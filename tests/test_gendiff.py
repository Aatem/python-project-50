from gendiff.generator_diff import generate_diff


def test_gendiff_json():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    true_result = open('tests/fixtures/true_result').read()
    assert result == true_result

def test_gendiff_yaml():
    result_yaml = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
    true_result = open('tests/fixtures/true_result').read()
    assert result_yaml == true_result

def test_gendiff_yml():
    result_yaml = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    true_result = open('tests/fixtures/true_result').read()
    assert result_yaml == true_result

def test_gendiff_json2():
    result = generate_diff('tests/fixtures/file11.json', 'tests/fixtures/file22.json')
    true_result = open('tests/fixtures/true_result_2').read()
    assert result == true_result

def test_gendiff_yml2():
    result = generate_diff('tests/fixtures/file11.yml', 'tests/fixtures/file22.yml')
    true_result = open('tests/fixtures/true_result_2').read()
    assert result == true_result

def test_gendiff_yaml2():
    result = generate_diff('tests/fixtures/file11.yaml', 'tests/fixtures/file22.yaml')
    true_result = open('tests/fixtures/true_result_2').read()
    assert result == true_result

