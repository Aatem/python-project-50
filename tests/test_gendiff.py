import pytest
from gendiff.generator_diff import generate_diff


file1 = 'tests/fixtures/file1.'
file2 = 'tests/fixtures/file2.'
file11 = 'tests/fixtures/file11.'
file22 = 'tests/fixtures/file22.'
true_result = 'tests/fixtures/true_result'
true_result_2 = 'tests/fixtures/true_result_2'
true_result_3 = 'tests/fixtures/true_result_3'
true_result_json = 'tests/fixtures/true_result.json'
files_to_pytest = [
    (file1 + 'json', file2 + 'json', 'stylish', true_result),
    (file1 + 'yaml', file2 + 'yaml', 'stylish', true_result),
    (file1 + 'yml', file2 + 'yml', 'stylish', true_result),
    (file11 + 'json', file22 + 'json', 'stylish', true_result_2),
    (file11 + 'yaml', file22 + 'yaml', 'stylish', true_result_2),
    (file11 + 'yml', file22 + 'yml', 'stylish', true_result_2),
    (file11 + 'json', file22 + 'json', 'plain', true_result_3),
    (file11 + 'yaml', file22 + 'yaml', 'plain', true_result_3),
    (file11 + 'yml', file22 + 'yml', 'plain', true_result_3),
    (file11 + 'json', file22 + 'json', 'json', true_result_json),
    (file11 + 'yaml', file22 + 'yaml', 'json', true_result_json),
    (file11 + 'yml', file22 + 'yml', 'json', true_result_json)]


@pytest.mark.parametrize('input1,input2,formatter,output', files_to_pytest)
def test_gendiff(input1, input2, formatter, output):
    assert generate_diff(input1, input2, formatter) == open(output).read()
