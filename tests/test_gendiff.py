from gendiff.generator_diff import generate_diff


def test_gendiff_json():
    
    result_json = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    true_result_json = open('tests/fixtures/true_result').read()
    assert result_json == true_result_json

def test_gendiff_yaml():
    result_yaml = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
    true_result_yaml = open('tests/fixtures/true_result').read()
    assert result_yaml == true_result_yaml