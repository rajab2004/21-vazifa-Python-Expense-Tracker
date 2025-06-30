## 💼 Expense Tracker – Mini Project

### 🎯 Maqsad:

Foydalanuvchi har kuni qancha pul sarflaganini yozadi. Loyihada foydalanuvchi xarajatlarni qo‘shadi, hammasini ko‘radi, umumiy summani hisoblaydi va sanaga yoki turga qarab filtrlaydi.

---

## 📁 Fayl: `expenses.csv`

Har bir qatorda:

```
date,category,amount
```

Misol:

```
2025-06-30,Food,25000
2025-06-30,Transport,7000
2025-06-29,Entertainment,15000
```

---

## 🧭 Funksiyalar:

1. Add new expense
2. View all expenses
3. View total expenses
4. Filter by date
5. Filter by category
6. Exit

---

## 🧠 O‘rgatiladigan asosiy tushunchalar:

| Tushuncha          | Qayerda ishlatilgan                   |
| ------------------ | ------------------------------------- |
| `open()`           | Fayl ochish va yozish (`"a"`, `"r"`)  |
| `split()`          | Qatorni ustunlarga ajratish           |
| `with`             | Faylni xavfsiz ochish                 |
| `float()`          | Sonlarni matndan raqamga aylantirish  |
| `os.path.exists()` | Fayl bor yoki yo‘qligini tekshirish   |
| `strip()`          | Qator oxiridagi `\n` ni olib tashlash |

---
