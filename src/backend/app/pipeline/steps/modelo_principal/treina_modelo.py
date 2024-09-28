from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score


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

def execute(df_merged):
    '''
    Script to build the GRU model for classification and train it.

    Parameters:
    df_merged: pandas DataFrame

    Returns:
    Sequential: Trained Keras model.
    '''
    X_train, X_test, y_train, y_test = preparacao_dados(df_merged)
    # Building the GRU model
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

    # Training the model
    model.fit(
        X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test)
    )

    y_pred = model.predict(X_test)

    y_pred = (y_pred > 0.5).astype(int).flatten()

    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)

    model.save("./pipeline/model.h5")

    return {
        "model_name": "GRU",
        "type_model": "Main Model",
        "metrics": {
            "accuracy": float(accuracy),  
            "recall": float(recall),     
            "f1": float(f1),
            "precision": float(precision),           
        }
    }