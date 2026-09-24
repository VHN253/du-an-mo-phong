class Agent:
    def __init__(self, ten, noi_tinh):
        self.ten = ten
        self.suc_khoe = 100
        self.nang_luong = 100
        self.tuoi = 0
        self.thoi_gian_song = 0     
        self.doi = 0
        self.toc_do = 5                
        self.do_dai_buoc = 1           
        self.noi_tinh = noi_tinh

    def tien_hoa_thoi_gian(self, so_gio):
        self.thoi_gian_song += so_gio
        tuoi_moi = so_gio / 8766
        self.tuoi += tuoi_moi
        self.doi += so_gio * 2
        if self.doi > 100:
            self.doi = 100
        if self.doi > 80:
            self.suc_khoe -= 5

    def di_chuyen(self, so_buoc):
        quang_duong = so_buoc * self.do_dai_buoc
        thoi_gian = quang_duong / (self.toc_do * 1000)
        if self.noi_tinh == "nóng tính":
            hao_nang_luong = so_buoc * 1
        else:
            hao_nang_luong = so_buoc * 0.5

        self.nang_luong -= hao_nang_luong
        self.tien_hoa_thoi_gian(thoi_gian)

    def nghi_ngay(self, gio):
        thoi_gian = gio
        self.nang_luong += gio * 5
        if self.nang_luong > 100:
            self.nang_luong = 100
        self.tien_hoa_thoi_gian(thoi_gian)


    def an(self):
        self.doi -= 30
        if self.doi < 0:
            self.doi = 0

    def hien_thi_thong_tin(self):
        print("Tên:", self.ten)
        print("Tuổi:", int(self.tuoi))
        print("Sức Khỏe:", self.suc_khoe)
        print("Năng Lượng:", self.nang_luong)
        print("Mức đói:", f"{self.doi:.2f}")
        print("Nội tính:", self.noi_tinh)


Agent1 = Agent("001", "Hiền")
Agent2 = Agent("002", "nóng tính")

Agent1.di_chuyen(50)
Agent1.nghi_ngay(3)
Agent2.di_chuyen(100)

print("==== TRƯỚC KHI ĂN ====")
Agent1.hien_thi_thong_tin()

Agent1.an()
Agent1.an()

print("==== SAU KHI ĂN ====")
Agent1.hien_thi_thong_tin()
Agent2.hien_thi_thong_tin()