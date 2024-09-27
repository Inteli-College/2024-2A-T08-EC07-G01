from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
import numpy as np
from sklearn.model_selection import train_test_split


def preparacao_dados(df):
    # Separando as features (X) e o target (y)
    X = df.drop(
        columns=["FALHA", "KNR"]
    )  # 'KNR' é apenas um identificador, então deve ser removido
    y = df["FALHA"]
    # Separando em dados de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    # Converte X_train e X_test para arrays NumPy, caso ainda não sejam.
    X_train = np.array(X_train)
    X_test = np.array(X_test)

    # Reestrutura X_train e X_test para ter 3 dimensões.
    # A nova forma do array será (n_samples, n_features, 1)
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

    return X_train, X_test, y_train, y_test


def execute(df):
    X_train, X_test, y_train, y_test = preparacao_dados(df)
    # Construção do modelo com GRU
    model = Sequential()

    model.add(
        GRU(
            50,
            activation="relu",
            return_sequences=True,
            input_shape=(X_train.shape[1], 1),
        )
    )
    model.add(GRU(50, activation="relu"))
    model.add(Dense(1, activation="sigmoid"))

    model.compile(optimizer="adam", loss="binary_crossentropy")

    # Treinamento do modelo
    model.fit(
        X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test)
    )

    return model
