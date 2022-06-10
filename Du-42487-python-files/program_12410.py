from math import ceil

def main():

    # Sample marks in each CA component
    labs = 75
    labexam_01 = 25
    labexam_02 = 32
    bucket_list = 100

    ca = (2 * labs) + (3 * labexam_01) + (3 * labexam_02) + (2 * bucket_list)

    ca  = ceil(ca/10)

    print(('Your final CA mark is: {:.0%}'.format(ca/100)))

if __name__ == "__main__":
    main()

