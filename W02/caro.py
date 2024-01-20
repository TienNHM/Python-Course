'''
Viết chương trình mô phỏng trò chơi caro sử dụng hàm và cấu list để lưu trữ dữ liệu
Gợi ý: Viết hàm nhập giá trị từng người chơi chọn, viết hàm kiểm tra xem có có người chơi nào thắng chưa, 
nếu thắng thông báo người thắng, kết thúc chương trình. In ra bàn cờ hiện tại nếu chưa có người thắng.
- Input: 
    + 2 số nguyên dương n, m cho biết kích thước của bàn cờ (n hàng, m cột, m, n >= 5)
    + 1 số nguyên dương k cho biết số lượng ký tự liên tiếp cần để thắng
    + Lần lượt là tọa độ của 2 người chơi (x, y)
- Output:
    + Bàn cờ có kích thước n x m
    + Kết quả trò chơi
'''

def khoi_tao_ban_co(n: int, m: int):
    ban_co = list()
    for i in range(n):
        hang = []
        for j in range(m):
            hang.append(' ')
        ban_co.append(hang)
    return ban_co

def in_ban_co(ban_co: list):
    for hang in ban_co:
        for o in hang:
            print(o, end=' | ')
        print()
        print('-' * (len(hang) * 4 - 1))


def nhap_gia_tri(nguoi_choi: str, ban_co: list):
    while True:
        x = input(f"Nhập tọa độ hàng {nguoi_choi} (x >= 0): ")
        y = input(f"Nhập tọa độ cột {nguoi_choi} (y >= 0): ")
        if not x.isdigit() or not y.isdigit():
            print("Tọa độ không hợp lệ, vui lòng nhập lại!")
            continue
        x = int(x)
        y = int(y)
        if x < 0 or x >= len(ban_co[0]) or y < 0 or y >= len(ban_co[1]):
            print("Tọa độ không hợp lệ, vui lòng nhập lại!")
        elif ban_co[x][y] != ' ':
            print("Tọa độ đã được chọn, vui lòng nhập lại!")
        else:
            # ban_co[x][y] = nguoi_choi
            # dùng hàm để thay thế giá trị trong list
            hang_x = list(ban_co[x])
            hang_x[y] = nguoi_choi
            ban_co.pop(x)
            ban_co.insert(x, hang_x)
            
            break

def kiem_tra_thang(ban_co: list):
    # Kiểm tra hàng ngang
    for i in range(len(ban_co)):
        for j in range(len(ban_co[0]) - 4):
            if ban_co[i][j] != ' ':
                for l in range(1, 5):
                    if ban_co[i][j] != ban_co[i][j + l]:
                        break
                else:
                    return True
    # Kiểm tra hàng dọc
    for i in range(len(ban_co[0])):
        for j in range(len(ban_co) - 4):
            if ban_co[j][i] != ' ':
                for l in range(1, 5):
                    if ban_co[j][i] != ban_co[j + l][i]:
                        break
                else:
                    return True
    # Kiểm tra đường chéo chính
    for i in range(len(ban_co) - 4):
        for j in range(len(ban_co[0]) - 4):
            if ban_co[i][j] != ' ':
                for l in range(1, 5):
                    if ban_co[i][j] != ban_co[i + l][j + l]:
                        break
                else:
                    return True
    # Kiểm tra đường chéo phụ
    for i in range(len(ban_co) - 4):
        for j in range(4, len(ban_co[0])):
            if ban_co[i][j] != ' ':
                for l in range(1, 5):
                    if ban_co[i][j] != ban_co[i + l][j - l]:
                        break
                else:
                    return True
    return False

if __name__ == '__main__':
    # Nhập kích thước bàn cờ, m, n >= 5
    while True:
        n = int(input("Nhập số hàng: "))
        m = int(input("Nhập số cột: "))
        if n >= 5 and m >= 5:
            break
        else:
            print("Kích thước bàn cờ không hợp lệ, vui lòng nhập lại!")

    ban_co = khoi_tao_ban_co(n, m)
    in_ban_co(ban_co)

    while True:
        nhap_gia_tri('X', ban_co)
        in_ban_co(ban_co)
        if kiem_tra_thang(ban_co):
            print("Người chơi X thắng!")
            break

        nhap_gia_tri('O', ban_co)
        in_ban_co(ban_co)
        if kiem_tra_thang(ban_co):
            print("Người chơi O thắng!")
            break

