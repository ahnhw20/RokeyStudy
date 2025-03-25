import tkinter as tk
from tkinter import messagebox

# 피자 조각당 가격 설정
SLICE_PRICE = 3000

def calculate_total():
    """총 가격 계산"""
    try:
        slices = int(slice_var.get())
        if slices < 1:
            raise ValueError
        total_price = slices * SLICE_PRICE
        total_label.config(text=f"총 가격: {total_price}원")
    except ValueError:
        messagebox.showerror("입력 오류", "올바른 조각 수를 입력하세요.")

def place_order():
    """주문 완료 처리"""
    slices = slice_var.get()
    if not slices.isdigit() or int(slices) < 1:
        messagebox.showerror("주문 오류", "1개 이상의 조각을 선택하세요.")
        return
    
    total_price = int(slices) * SLICE_PRICE
    messagebox.showinfo("주문 완료", f"{slices} 조각의 피자를 주문했습니다!\n총 가격: {total_price}원")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("피자 조각 주문 프로그램")
root.geometry("300x250")

# 라벨
tk.Label(root, text="조각 피자 주문", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="몇 조각을 주문하시겠습니까?", font=("Arial", 12)).pack()

# 입력 필드
slice_var = tk.StringVar()
slice_entry = tk.Entry(root, textvariable=slice_var, font=("Arial", 12))
slice_entry.pack(pady=5)

# 총 가격 표시 라벨
total_label = tk.Label(root, text="총 가격: 0원", font=("Arial", 12, "bold"), fg="red")
total_label.pack(pady=5)

# 버튼
tk.Button(root, text="가격 계산", command=calculate_total, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="주문하기", command=place_order, font=("Arial", 12), bg="green", fg="white").pack(pady=5)

# Tkinter 실행
root.mainloop()
