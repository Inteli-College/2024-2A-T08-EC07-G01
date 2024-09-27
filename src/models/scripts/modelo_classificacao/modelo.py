import models.scripts.preparacao as preparacao
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense


def execute(df):
    '''
    Script to build the GRU model for classification and train it.

    Parameters:
    df: pandas DataFrame
    '''
    X_train, X_test, y_train, y_test = preparacao.preparacao_dados(df)
    model = Sequential()

    model.add(GRU(50, activation='relu', return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(GRU(50, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy')

    model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

    return model

    # # Prever os dados de teste
    # y_pred = model.predict(X_test)

    # # Converter as probabilidades em classes binárias (0 ou 1)
    # y_pred_classes = (y_pred > 0.5).astype(int)

    # # Calcular as principais métricas
    # accuracy_2 = accuracy_score(y_test, y_pred_classes)
    # precision_2 = precision_score(y_test, y_pred_classes)
    # recall_2 = recall_score(y_test, y_pred_classes)
    # f1_2 = f1_score(y_test, y_pred_classes)