import streamlit as st

# タイトルの表示
st.title("お釣り計算ツール(WEB版)")

# 入力フォーム(数値のみを受け付けるボックス)
# ステップが1なので、+-ボタンで1円ずつ調整できます
price = st.number_input("商品の代金を入力してください", min_value=0, step=1, value=100)

# ボタンの作成と、押されたときの処理
if st.button("計算を実行する"):
    # 計算ロジック
    pay50 = price + 50
    pay100 = price + 100
    pay500 = price + 500

    # 画面に見やすく表示
    st.divider()    # 区切り線
    st.subheader("おすすめの支払額")
    st.write(f"50円玉がほしいとき：　**{pay50}円**")
    st.write(f"100円玉がほしいとき：　**{pay100}円**")
    st.write(f"500円玉がほしいとき：　**{pay500}円**")
