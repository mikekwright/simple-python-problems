def get_number():
    while True:
        value = input('Give me a number: ')
        try:
            int_value = int(value)
            return int_value
        except Exception:
            print('Enter a valid number')


def output_total(total):
    print()
    print(f'Total: {total}')


def main():
    # Put your code here
    # Delete pass once you are done
    pass


if __name__ == '__main__':
    main()

