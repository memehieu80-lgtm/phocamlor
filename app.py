import streamlit as st
from datetime import datetime

# =========================================================
# CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="Phở Việt - Quản lý quán phở",
    page_icon="🍜",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #fffaf3;
}

.header {
    background: linear-gradient(135deg, #b71c1c, #e65100);
    padding: 30px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.header h1 {
    font-size: 45px;
    margin-bottom: 5px;
}

.header p {
    font-size: 18px;
}

.food-card {
    background: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.10);
    margin-bottom: 15px;
}

.price {
    color: #d32f2f;
    font-size: 20px;
    font-weight: bold;
}

.info-box {
    background: #fff3e0;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 15px;
}

.bill {
    background: #ffffff;
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #eeeeee;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# THÔNG TIN QUÁN
# =========================================================

TEN_QUAN = "PHỞ GIA TRUYỀN VIỆT"

DIA_CHI = "123 Đại lộ Bình Dương, Thủ Dầu Một, Bình Dương"

SDT_QUAN = "0901 234 567"

ANH_BIA = (
    "https://images.unsplash.com/"
    "photo-1601050690597-df0568f70950"
    "?auto=format&fit=crop&w=1600&q=80"
)


# =========================================================
# DANH SÁCH MÓN PHỞ
# =========================================================

MENU = {

    "Phở Bò Tái": {
        "gia": 55000,
        "mo_ta": "Nước dùng bò trong, thơm, kết hợp thịt bò tái mềm và bánh phở dai.",
        "thanh_phan": "Bánh phở, thịt bò tái, hành lá, hành tây, rau thơm.",
        "anh": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=800&q=80"
    },

    "Phở Bò Chín": {
        "gia": 55000,
        "mo_ta": "Thịt bò được ninh chín mềm, nước dùng đậm đà và thơm mùi quế hồi.",
        "thanh_phan": "Bánh phở, bò chín, hành lá, hành tây, rau thơm.",
        "anh": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=800&q=80"
    },

    "Phở Tái Nạm": {
        "gia": 60000,
        "mo_ta": "Kết hợp thịt bò tái mềm và nạm bò béo nhẹ.",
        "thanh_phan": "Bánh phở, bò tái, nạm bò, hành lá, hành tây.",
        "anh": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=800&q=80"
    },

    "Phở Tái Gầu": {
        "gia": 65000,
        "mo_ta": "Thịt bò tái kết hợp gầu bò thơm béo.",
        "thanh_phan": "Bánh phở, bò tái, gầu bò, hành lá, hành tây, rau thơm.",
        "anh": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=800&q=80"
    },

    "Phở Bò Đặc Biệt": {
        "gia": 75000,
        "mo_ta": "Tô phở đầy đủ với nhiều loại thịt bò.",
        "thanh_phan": "Tái, nạm, gầu, bò viên, bánh phở và rau thơm.",
        "anh": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=800&q=80"
    },

    "Phở Gà": {
        "gia": 55000,
        "mo_ta": "Nước dùng gà thanh nhẹ, thịt gà mềm và thơm.",
        "thanh_phan": "Bánh phở, thịt gà, hành lá, hành tây, rau thơm.",
        "anh": "https://images.unsplash.com/photo-1601050690117-94f5f6fa8bd7?auto=format&fit=crop&w=800&q=80"
    },

    "Phở Gà Đặc Biệt": {
        "gia": 70000,
        "mo_ta": "Tô phở gà đầy đủ với nhiều phần thịt gà.",
        "thanh_phan": "Thịt gà, da gà, bánh phở, hành lá, hành tây.",
        "anh": "https://images.unsplash.com/photo-1601050690117-94f5f6fa8bd7?auto=format&fit=crop&w=800&q=80"
    },

    "Phở Bò Viên": {
        "gia": 55000,
        "mo_ta": "Phở bò viên với nước dùng thơm và bò viên dai ngon.",
        "thanh_phan": "Bánh phở, bò viên, hành lá, hành tây, rau thơm.",
        "anh": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=800&q=80"
    },

    "Phở Không Thịt": {
        "gia": 35000,
        "mo_ta": "Phù hợp với khách muốn thưởng thức nước dùng và bánh phở.",
        "thanh_phan": "Bánh phở, hành lá, hành tây, rau thơm.",
        "anh": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=800&q=80"
    }
}


# =========================================================
# NHÂN VIÊN
# =========================================================

NHAN_VIEN = [
    {
        "ten": "Nguyễn Văn An",
        "chuc_vu": "Quản lý",
        "sdt": "0902 111 222"
    },
    {
        "ten": "Trần Minh Anh",
        "chuc_vu": "Thu ngân",
        "sdt": "0903 222 333"
    },
    {
        "ten": "Lê Văn Bình",
        "chuc_vu": "Đầu bếp",
        "sdt": "0904 333 444"
    },
    {
        "ten": "Phạm Thị Hoa",
        "chuc_vu": "Phục vụ",
        "sdt": "0905 444 555"
    }
]


# =========================================================
# BÀN
# =========================================================

SO_BAN = 20

BAN = {
    f"Bàn {i}": "Trống"
    for i in range(1, SO_BAN + 1)
}


# =========================================================
# SESSION STATE
# =========================================================

if "gio_hang" not in st.session_state:
    st.session_state.gio_hang = {}

if "luot_khach" not in st.session_state:
    st.session_state.luot_khach = 1286


# =========================================================
# HEADER
# =========================================================

st.image(ANH_BIA, use_container_width=True)

st.markdown(f"""
<div class="header">
    <h1>🍜 {TEN_QUAN}</h1>
    <p>Hương vị phở truyền thống Việt Nam</p>
    <p>📍 {DIA_CHI}</p>
    <p>☎ {SDT_QUAN}</p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# THÔNG TIN TỔNG QUAN
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("👥 Lượt khách", st.session_state.luot_khach)

with c2:
    st.metric("🪑 Số bàn", SO_BAN)

with c3:
    st.metric("🍜 Số món", len(MENU))

with c4:
    st.metric("👨‍🍳 Nhân viên", len(NHAN_VIEN))


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🍜 QUẢN LÝ QUÁN PHỞ")

lua_chon = st.sidebar.radio(
    "Chọn chức năng",
    [
        "🍜 Thực đơn",
        "🛒 Đặt món",
        "🧾 Thanh toán",
        "🪑 Quản lý bàn",
        "👨‍🍳 Nhân viên",
        "ℹ️ Thông tin quán"
    ]
)


# =========================================================
# THỰC ĐƠN
# =========================================================

if lua_chon == "🍜 Thực đơn":

    st.title("🍜 THỰC ĐƠN QUÁN PHỞ")

    for ten_mon, thong_tin in MENU.items():

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(
                thong_tin["anh"],
                use_container_width=True
            )

        with col2:

            st.subheader(ten_mon)

            st.markdown(
                f"<div class='price'>"
                f"{thong_tin['gia']:,} VNĐ"
                f"</div>",
                unsafe_allow_html=True
            )

            st.write(
                "**Mô tả:**",
                thong_tin["mo_ta"]
            )

            st.write(
                "**Thành phần:**",
                thong_tin["thanh_phan"]
            )

            st.divider()


# =========================================================
# ĐẶT MÓN
# =========================================================

elif lua_chon == "🛒 Đặt món":

    st.title("🛒 ĐẶT MÓN")

    col1, col2 = st.columns(2)

    with col1:

        ten_khach = st.text_input(
            "👤 Tên khách hàng"
        )

        sdt_khach = st.text_input(
            "📱 Số điện thoại"
        )

    with col2:

        ban = st.selectbox(
            "🪑 Chọn bàn",
            list(BAN.keys())
        )

        nhan_vien = st.selectbox(
            "👨‍🍳 Nhân viên phục vụ",
            [
                nv["ten"]
                for nv in NHAN_VIEN
            ]
        )

    st.divider()

    st.subheader("🍜 Chọn món")

    mon = st.selectbox(
        "Chọn món ăn",
        list(MENU.keys())
    )

    so_luong = st.number_input(
        "Số lượng",
        min_value=1,
        max_value=20,
        value=1
    )

    if st.button("➕ THÊM VÀO GIỎ", use_container_width=True):

        if mon in st.session_state.gio_hang:
            st.session_state.gio_hang[mon] += so_luong
        else:
            st.session_state.gio_hang[mon] = so_luong

        st.success(
            f"Đã thêm {so_luong} {mon} vào giỏ hàng!"
        )

    st.divider()

    st.subheader("🛒 GIỎ HÀNG")

    tong_tien = 0

    if len(st.session_state.gio_hang) == 0:

        st.info("Chưa có món nào.")

    else:

        for ten_mon, so_luong in st.session_state.gio_hang.items():

            gia = MENU[ten_mon]["gia"]

            thanh_tien = gia * so_luong

            tong_tien += thanh_tien

            st.write(
                f"🍜 {ten_mon} × {so_luong} "
                f"= **{thanh_tien:,} VNĐ**"
            )

        st.markdown(
            f"""
            ### 💰 TỔNG TIỀN: {tong_tien:,} VNĐ
            """
        )


# =========================================================
# THANH TOÁN
# =========================================================

elif lua_chon == "🧾 Thanh toán":

    st.title("🧾 THANH TOÁN")

    if len(st.session_state.gio_hang) == 0:

        st.warning(
            "Chưa có món ăn trong giỏ hàng."
        )

    else:

        tong_tien = 0

        st.markdown(
            "<div class='bill'>",
            unsafe_allow_html=True
        )

        st.subheader("🍜 HÓA ĐƠN")

        st.write(
            f"**Quán:** {TEN_QUAN}"
        )

        st.write(
            f"**Địa chỉ:** {DIA_CHI}"
        )

        st.write(
            f"**Thời gian:** "
            f"{datetime.now().strftime('%d/%m/%Y %H:%M')}"
        )

        st.divider()

        for ten_mon, so_luong in st.session_state.gio_hang.items():

            gia = MENU[ten_mon]["gia"]

            thanh_tien = gia * so_luong

            tong_tien += thanh_tien

            st.write(
                f"{ten_mon} × {so_luong}: "
                f"{thanh_tien:,} VNĐ"
            )

        st.divider()

        st.subheader(
            f"TỔNG CỘNG: {tong_tien:,} VNĐ"
        )

        tien_khach = st.number_input(
            "💵 Tiền khách đưa",
            min_value=0,
            step=10000
        )

        if tien_khach >= tong_tien:

            tien_thua = tien_khach - tong_tien

            st.success(
                f"💰 Tiền thừa: {tien_thua:,} VNĐ"
            )

        else:

            con_thieu = tong_tien - tien_khach

            st.error(
                f"⚠️ Khách còn thiếu: "
                f"{con_thieu:,} VNĐ"
            )

        if st.button(
            "✅ HOÀN TẤT THANH TOÁN",
            use_container_width=True
        ):

            st.session_state.luot_khach += 1

            st.session_state.gio_hang = {}

            st.success(
                "Thanh toán thành công!"
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# =========================================================
# QUẢN LÝ BÀN
# =========================================================

elif lua_chon == "🪑 Quản lý bàn":

    st.title("🪑 QUẢN LÝ BÀN")

    cols = st.columns(4)

    for index, (ten_ban, trang_thai) in enumerate(BAN.items()):

        with cols[index % 4]:

            st.markdown(
                f"""
                <div class="info-box">
                    <h3>🪑 {ten_ban}</h3>
                    <p>Trạng thái: <b>{trang_thai}</b></p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.info(
        f"Quán hiện có tổng cộng {SO_BAN} bàn."
    )


# =========================================================
# NHÂN VIÊN
# =========================================================

elif lua_chon == "👨‍🍳 Nhân viên":

    st.title("👨‍🍳 DANH SÁCH NHÂN VIÊN")

    for nv in NHAN_VIEN:

        st.markdown(
            f"""
            <div class="food-card">
                <h3>👤 {nv['ten']}</h3>
                <p>💼 Chức vụ: {nv['chuc_vu']}</p>
                <p>📱 Số điện thoại: {nv['sdt']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# THÔNG TIN QUÁN
# =========================================================

elif lua_chon == "ℹ️ Thông tin quán":

    st.title("ℹ️ THÔNG TIN QUÁN")

    st.image(
        ANH_BIA,
        use_container_width=True
    )

    st.markdown(
        f"""
        ## 🍜 {TEN_QUAN}

        **📍 Địa chỉ:** {DIA_CHI}

        **☎ Số điện thoại:** {SDT_QUAN}

        **🪑 Số bàn:** {SO_BAN}

        **👨‍🍳 Số nhân viên:** {len(NHAN_VIEN)}

        **👥 Lượt khách:** {st.session_state.luot_khach}

        **🍜 Số lượng món:** {len(MENU)}

        ### Giới thiệu

        {TEN_QUAN} chuyên phục vụ các món phở
        truyền thống Việt Nam với nước dùng được
        ninh từ xương, kết hợp thịt bò, thịt gà
        và các loại rau thơm.

        Quán phục vụ ăn tại chỗ, phù hợp cho
        khách cá nhân, gia đình và nhóm bạn.
        """
    )

    st.divider()

    st.subheader("📞 Liên hệ")

    st.write(
        f"Điện thoại: {SDT_QUAN}"
    )

    st.write(
        f"Địa chỉ: {DIA_CHI}"
    )
