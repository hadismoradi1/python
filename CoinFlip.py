import random

print("شبیه ساز پرتاب سکه")

while True:
    try:
        n = int(input("چند بار سکه بندازم؟ (برای خروج 0)"))
        if n==0:
            print("خدافظ")
            break
        results = []
        for _ in range(n):
            toss = random.choice(["شیر", "خط"])
            results.append(toss)

        shir = results.count("شیر")
        khat = results.count("خط")

        shir_percent = (shir / n) * 100
        khat_percent = (khat / n) * 100

        print("نتایج","".join(results))
        print(f"📊 آمار: شیر = {shir} بار ({shir_percent:.1f}%) | خط = {khat} بار ({khat_percent:.1f}%)\n")

    except ValueError:
        print("❌ لطفا یک عدد صحیح وارد کنید!\n")