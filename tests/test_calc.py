from websockets.calc import calculador

def test_calculador():
    # When
    x = 1
    y = 2
    # Then
    result = 3
    # Act
    output = calculador(x,y)
    assert result == output


