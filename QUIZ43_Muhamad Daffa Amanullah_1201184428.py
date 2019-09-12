ListGPA = [2.1,2.5,4,3]

def Reward (GPA):
    bonus = 50000
    Reward = GPA*bonus
    return Reward

for GPA in ListGPA:
    if GPA > 2.5:
        print("SELAMAT! ANDA MENDAPAT REWARD : Rp", Reward(GPA))
    else :
        print("MAAF, SELAMAT MENCOBA LAGI!")