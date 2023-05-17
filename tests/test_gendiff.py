from gendiff.generator_diff import generate_diff


def test_gendiff_json():
    
    result_json = generate_diff('/home/artem/python-project-50/tests/fixtures/file1.json', '/home/artem/python-project-50/tests/fixtures/file2.json')
    true_result_json = open('/home/artem/python-project-50/tests/fixtures/true_result').read()
    assert result_json == true_result_json