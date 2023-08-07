def is_valid_password(password):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0
    for char in password:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    return vowel_count >= 1 and consonant_count >= 2


def generate_passwords(password_length, characters, current_password, index):
    if len(current_password) == password_length:
        if is_valid_password(current_password):
            print(current_password)
        return

    if index >= len(characters):
        return

    generate_passwords(password_length, characters, current_password + characters[index], index + 1)
    generate_passwords(password_length, characters, current_password, index + 1)


def main():
    L, C = map(int, input().split())
    characters = input().split()
    characters.sort()

    generate_passwords(L, characters, "", 0)


if __name__ == "__main__":
    main()