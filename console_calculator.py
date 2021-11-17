

def test_main():
    assert (main(('45 + 4 - 242442 + 32342'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))) == -210051)
    print('all checked')
    # assert main('')

def main(parsed_str):    
    answer = 0
    for i in range(len(parsed_str)):
        answer += int(parsed_str[i])
    return answer
if __name__ == '__main__':
    print("Give your expression: ")
    print(main(parsed_str = input().replace(' ', '').replace('--', '+').replace('-', '+-').split('+')))
    test_main()

