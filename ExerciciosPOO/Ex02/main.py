from gym_member import GymMember


def main() -> None:
    member_one = GymMember("Ana Silva")
    member_two = GymMember("Rui Costa")

    print(member_one.monthly_fee, member_two.monthly_fee)

    GymMember.monthly_fee = 35
    print(member_one.monthly_fee, member_two.monthly_fee)

    member_one.monthly_fee = 20
    print(member_one.monthly_fee, member_two.monthly_fee, GymMember.monthly_fee)


if __name__ == "__main__":
    main()
