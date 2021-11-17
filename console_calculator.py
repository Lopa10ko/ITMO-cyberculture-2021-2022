def main():
    print("Give your expression: ")
    parsed_str = input().replace(' ', '').replace('--', '+').replace('-', '+-').split('+')
    answer = 0
    for i in range(len(parsed_str)):
        answer += int(parsed_str[i])
    print('Your answer: ', answer)
if __name__ == '__main__':
    main()


# def test_main():
#     assert main()