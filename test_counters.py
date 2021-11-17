import subprocess
import re

def test(draw_type, expected):
    print(draw_type)
    print(f'  expected: {expected}')
    output = subprocess.check_output(f'./debug.sh {draw_type}', shell=True, stderr=subprocess.PIPE)
    actual = [float(v) for v in re.findall(b'\{Counter:\d+ Value:([0-9.]+)\}', output)]
    print(f'  actual: {actual}')
    if len(actual) != len(expected):
        print('  FAIL')
        exit(1)
    for e_value, a_value in zip(expected, actual):
        if abs(e_value - a_value) > 0.01:
            print('  FAIL')
            exit(1)
    print('  PASS')



    


test("vkCmdDraw",                     [36, 12, 32, 36*32, 36*32/12])
test("vkCmdDrawIndirect",             [36, 12, 32, 36*32, 36*32/12])
test("vkCmdDrawIndirectCount",        [36, 12, 32, 36*32, 36*32/12])

test("vkCmdDrawIndexed",              [36, 12, 32, 36*(32+4), 36*(32+4)/12])
test("vkCmdDrawIndexedIndirect",      [36, 12, 32, 36*(32+4), 36*(32+4)/12])
test("vkCmdDrawIndexedIndirectCount", [36, 12, 32, 36*(32+4), 36*(32+4)/12])

test("vkCmdDrawIndexedRestart",       [29, 12, 32, 29*(32+4), 29*(32+4)/12])