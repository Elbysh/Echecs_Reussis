from unittest.mock import Mock
from _pytest.monkeypatch import MonkeyPatch
from game_chess.game_input import read_player_command


def mock_input_return(inputs):
    return Mock(side_effect=inputs)


def test_read_player_command():
    monkeypatch = MonkeyPatch()

    monkeypatch.setattr(
        'builtins.input', mock_input_return(['e2', 'y', 'e4', 'y']))
    # On test pour un coup allant de e2 à e4
    expected_output = [(6, 4), (4, 4)]
    result = read_player_command()
    assert result == expected_output
    monkeypatch.setattr(
        'builtins.input', mock_input_return(['e2', 'y', 'e4', 'y']))
    # On test pour un coup allant de e2 à e4
    expected_output = [(6, 4), (4, 4)]
    result = read_player_command()
    assert result == expected_output

    # On reteste dans d'autre cas, cette fois avec des erreurs humaines
    monkeypatch.setattr(
        'builtins.input', mock_input_return(['x48', 'e4', 'y', 'e4', 'y', 'e2', 'y', 'e3', 'y']))
    expected_output = [(6, 4), (5, 4)]
    result = read_player_command()
    assert result == expected_output
    # On reteste dans d'autre cas, cette fois avec des erreurs humaines
    monkeypatch.setattr(
        'builtins.input', mock_input_return(['x48', 'e4', 'y', 'e4', 'y', 'e2', 'y', 'e3', 'y']))
    expected_output = [(6, 4), (5, 4)]
    result = read_player_command()
    assert result == expected_output

    # On test le cas où les coordonées entréé sont 2 fois la même
    monkeypatch.setattr(
        'builtins.input', mock_input_return(['a1', 'y', 'a1', 'y', 'a2', 'y', 'e4', 'y']))
    expected_output = [(6, 0), (4, 4)]
    result = read_player_command()
    assert result == expected_output
    # On test le cas où les coordonées entréé sont 2 fois la même
    monkeypatch.setattr(
        'builtins.input', mock_input_return(['a1', 'y', 'a1', 'y', 'a2', 'y', 'e4', 'y']))
    expected_output = [(6, 0), (4, 4)]
    result = read_player_command()
    assert result == expected_output

    # Encore quelques tests pour tester toute l'arborescence
    monkeypatch.setattr(
        'builtins.input', mock_input_return(['a1', 'n', 'a2', 'y', 'e4', 'y']))

    expected_output = [(6, 0), (4, 4)]
    result = read_player_command()
    assert result == expected_output

    monkeypatch.setattr(
        'builtins.input', mock_input_return(['a1', 'y', 'a2', 'n', 'e4', 'y', 'e5', 'y']))

    expected_output = [(4, 4), (3, 4)]
    result = read_player_command()
    assert result == expected_output

    monkeypatch.setattr(
        'builtins.input', mock_input_return(['a1', 'y', 'i1', 'e4', 'y', 'e5', 'y']))

    expected_output = [(4, 4), (3, 4)]
    result = read_player_command()
    assert result == expected_output

    monkeypatch.setattr(
        'builtins.input', mock_input_return([1, 'e4', 'y', 'e5', 'y']))

    expected_output = [(4, 4), (3, 4)]
    result = read_player_command()
    assert result == expected_output

    monkeypatch.undo()


test_read_player_command()
