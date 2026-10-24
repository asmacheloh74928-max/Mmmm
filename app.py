import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="Logic Learning Hub - ตรรกศาสตร์เชิงคณิตศาสตร์",
    page_icon="🧠",
    layout="wide",
)

# ตกแต่ง CSS ให้ UI สวยงามสะอาดตาแบบโมเดิร์น
st.markdown(
    """
    <style>
    .main-title {
        font-size: 1.8rem;
        color: #2c3e50;
        font-weight: 700;
        background: #ffffff;
        padding: 10px 20px;
        border-radius: 10px;
        border-left: 5px solid #e83e8c;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02);
        margin-bottom: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- SIDEBAR: เมนูด้านข้างแบบแบ่งหมวดหมู่ชัดเจน ---
st.sidebar.markdown("### 🌸 Logic Lab")
st.sidebar.caption("ห้องเรียนตรรกศาสตร์ดิจิทัล")
st.sidebar.markdown("---")
st.sidebar.markdown("📌 **เมนูหลัก (MAIN MENU)**")

menu = st.sidebar.radio(
    "เลือกหัวข้อ",
    (
        "01. ภาพรวม & ประพจน์",
        "02. ตัวเชื่อมตรรกศาสตร์",
        "03. ตารางความจริง (Truth Table)",
        "04. สูตรสมพากย์ (Equivalence)",
        "05. สัจนิรันดร์ & การอ้างเหตุผล",
        "06. ตัวบ่งปริมาณ (Quantifiers)",
        "07. สรุปสูตรแผ่นเดียว (Cheat Sheet)",
    ),
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.info(
    "👩‍🏫 **ผู้จัดทำ:**\n"
    "- นางสาวอัสมะ เจะเลาะ (6711070055)\n"
    "- นูรูลฮูดา เปาะแต (6711070068)\n"
    "คณะครุศาสตร์ สาขาคณิตศาสตร์ ม.ราชภัฏธนบุรี"
)


# ==================== 01. ภาพรวม & ประพจน์ ====================
if menu == "01. ภาพรวม & ประพจน์":
    st.markdown(
        '<p class="main-title">📌 01. ภาพรวมและประพจน์ (Introduction & Propositions)</p>',
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown(
            """
        <div class="card">
        <h4>💡 ประพจน์คืออะไร?</h4>
        <p><b>ประพจน์ (Proposition หรือ Statement)</b> คือ ประโยคบอกเล่าหรือปฏิเสธที่มีค่าความจริง (Truth Value) เป็น <b>จริง (T)</b> หรือ <b>เท็จ (F)</b> อย่างใดอย่างหนึ่งเท่านั้น</p>
        <hr>
        <p><b>ประโยคที่เป็นประพจน์:</b><br>
        • "เมื่อวานฝนตกที่บางกะปิ" (เป็นประพจน์ เพราะตรวจสอบความจริงได้)<br>
        • "1 มากกว่า 2" (เป็นประพจน์ มีค่าความจริงเป็น F)</p>
        <p><b>ประโยคที่ไม่เป็นประพจน์:</b><br>
        ประโยคคำถาม คำสั่ง ขอร้อง แสดงความปรารถนา หรืออุทาน เช่น <i>"กรุณางดส่งเสียงดัง"</i> หรือ <i>"ใครทำแก้วแตก?"</i></p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
        <div class="card">
        <h4>🎯 แบบฝึกหัดทดสอบความเข้าใจ</h4>
        <p>ประโยคในข้อใดต่อไปนี้ <b>เป็นประพจน์</b>?</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        ans_p1 = st.radio(
            "เลือกคำตอบ:",
            (
                "เลือกคำตอบ...",
                "ก. ห้ามเดินลัดสนามหญ้า",
                "ข. 5 + 7 = 12",
                "ค. คุณกำลังทำอะไรอยู่?",
            ),
            key="p1_quiz",
        )

        if ans_p1 != "เลือกคำตอบ...":
            if "ข. 5 + 7 = 12" in ans_p1:
                st.success(
                    "🎉 ถูกต้อง! '5 + 7 = 12' เป็นประโยคบอกเล่าที่มีค่าความจริงชัดเจน (เท็จ) จึงถือเป็นประพจน์"
                )
            else:
                st.error(
                    "❌ ยังไม่ถูกต้อง ประโยคคำสั่งและคำถามไม่ถือเป็นประพจน์ ลองใหม่อีกครั้งนะ"
                )


# ==================== 02. ตัวเชื่อมตรรกศาสตร์ ====================
elif menu == "02. ตัวเชื่อมตรรกศาสตร์":
    st.markdown(
        '<p class="main-title">🔗 02. ตัวเชื่อมทางตรรกศาสตร์ (Logical Connectives)</p>',
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
    <div class="card">
    <h4>📌 5 ตัวเชื่อมพื้นฐานและกฎการให้ค่าความจริง</h4>
    <ul>
        <li><b>นิเสธ ($\sim P$):</b> กลับค่าความจริงตรงกันข้าม</li>
        <li><b>และ ($P \wedge Q$):</b> เป็นจริงเฉพาะกรณีที่เป็นจริงทั้งคู่ นอกนั้นเป็นเท็จ</li>
        <li><b>หรือ ($P \vee Q$):</b> เป็นเท็จเฉพาะกรณีที่เป็นเท็จทั้งคู่ นอกนั้นเป็นจริง</li>
        <li><b>ถ้า...แล้ว ($P \rightarrow Q$):</b> เป็นเท็จกรณีเดียวคือ เมื่อ $T \rightarrow F$ นอกนั้นเป็นจริง</li>
        <li><b>ก็ต่อเมื่อ ($P \leftrightarrow Q$):</b> เป็นจริงเมื่อประพจน์ทั้งสองมีค่าความจริงเหมือนกัน</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.subheader("📝 ทดสอบความเข้าใจตัวเชื่อม")
    c_quiz = st.radio(
        "กำหนดให้ $P \equiv T$ และ $Q \equiv F$ จงหาค่าความจริงของ $P \rightarrow Q$",
        ("เลือกคำตอบ...", "True (T)", "False (F)"),
        key="conn_quiz",
    )
    if c_quiz != "เลือกคำตอบ...":
        if "False" in c_quiz:
            st.success(
                "🎉 ถูกต้อง! เพราะ $T \rightarrow F \equiv F$ เป็นกรณีเดียวที่ทำให้เงื่อนไขนี้เป็นเท็จ"
            )
        else:
            st.error(
                "❌ ยังไม่ถูกต้อง จำไว้ว่า 'จริงแล้วเท็จ ได้เท็จ' ($T \rightarrow F \equiv F$)"
            )


# ==================== 03. ตารางความจริง ====================
elif menu == "03. ตารางความจริง (Truth Table)":
    st.markdown(
        '<p class="main-title">📊 03. ตารางความจริง (Truth Table)</p>',
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
    <div class="card">
    <h4>💡 ตารางแสดงค่าความจริงของตัวเชื่อมทั้งหมด</h4>
    <p>จำนวนแถวในตารางคำนวณจากสูตร $2^n$ เมื่อ $n$ คือจำนวนประพจน์ย่อย</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    | P | Q | $\sim P$ | $P \wedge Q$ | $P \vee Q$ | $P \rightarrow Q$ | $P \leftrightarrow Q$ |
    |---|---|---------|------------|----------|-----------------|---------------------|
    | T | T | F       | T          | T        | T               | T                   |
    | T | F | F       | F          | T        | F               | F                   |
    | F | T | T       | F          | T        | T               | F                   |
    | F | F | T       | F          | F        | T               | T                   |
    """
    )


# ==================== 04. สูตรสมพากย์ ====================
elif menu == "04. สูตรสมพากย์ (Equivalence)":
    st.markdown(
        '<p class="main-title">🔄 04. รูปแบบประพจน์ที่สมมูลกัน (Logical Equivalences)</p>',
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
    <div class="card">
    <h4>📌 กฎสมมูลที่สำคัญ (Useful Identities)</h4>
    <ul>
        <li><b>Implication Law:</b> $P \rightarrow Q \equiv \sim P \vee Q$</li>
        <li><b>Contrapositive:</b> $P \rightarrow Q \equiv \sim Q \rightarrow \sim P$</li>
        <li><b>Biconditional:</b> $P \leftrightarrow Q \equiv (P \rightarrow Q) \wedge (Q \rightarrow P)$</li>
        <li><b>De Morgan's Laws:</b> $\sim(P \wedge Q) \equiv \sim P \vee \sim Q$ และ $\sim(P \vee Q) \equiv \sim P \wedge \sim Q$</li>
        <li><b>Double Negation:</b> $\sim(\sim P) \equiv P$</li>
    </ul>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ==================== 05. สัจนิรันดร์ & การอ้างเหตุผล ====================
elif menu == "05. สัจนิรันดร์ & การอ้างเหตุผล":
    st.markdown(
        '<p class="main-title">✨ 05. สัจนิรันดร์ (Tautology) และการอ้างเหตุผล (Arguments)</p>',
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown(
            """
        <div class="card">
        <h4>🔍 สัจนิรันดร์คืออะไร?</h4>
        <p><b>สัจนิรันดร์ (Tautology)</b> คือ ประพจน์ที่มีค่าความจริงเป็น <b>จริง (T) ทุกกรณี</b> ในตารางค่าความจริง</p>
        <hr>
        <p><b>วิธีตรวจสอบ:</b><br>
        1. ใช้ตารางความจริง (ดูว่าคอลัมน์สุดท้ายเป็น T ทั้งหมดหรือไม่)<br>
        2. วิธีหาข้อขัดแย้ง (นิยมมาก): สมมติให้ประพจน์รวมเป็น เท็จ (F) แล้วตรวจสอบว่าเกิดข้อขัดแย้งหรือไม่ ถ้าขัดแย้ง แสดงว่าเป็นสัจนิรันดร์</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col_b:
        st.markdown(
            """
        <div class="card">
        <h4>⚖️ การอ้างเหตุผล (Arguments)</h4>
        <p>ประกอบด้วย <b>เหตุ</b> ($P_1, P_2, \dots, P_n$) และ <b>ผล</b> ($C$)</p>
        <p>รูปแบบการเชื่อม: $(P_1 \wedge P_2 \wedge \dots \wedge P_n) \rightarrow C$ จะ<b>สมเหตุสมผล (Valid)</b> ก็ต่อเมื่อเป็นสัจนิรันดร์</p>
        <hr>
        <p><b>กฎการอ้างเหตุผลยอดฮิต:</b><br>
        • <b>Modus Ponens:</b> $P \rightarrow Q, P \vdash Q$<br>
        • <b>Modus Tollens:</b> $P \rightarrow Q, \sim Q \vdash \sim P$<br>
        • <b>Hypothetical Syllogism:</b> $P \rightarrow Q, Q \rightarrow R \vdash P \rightarrow R$</p>
        </div>
        """,
            unsafe_allow_html=True,
        )


# ==================== 06. ตัวบ่งปริมาณ ====================
elif menu == "06. ตัวบ่งปริมาณ (Quantifiers)":
    st.markdown(
        '<p class="main-title">🔍 06. ประโยคเปิดและตัวบ่งปริมาณ (Open Sentences & Quantifiers)</p>',
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
    <div class="card">
    <h4>📌 ตัวบ่งปริมาณ (Quantifiers)</h4>
    <ul>
        <li><b>สำหรับทุกคน ($\forall x P(x)$):</b> เป็นจริงเมื่อ $P(x)$ เป็นจริงสำหรับทุกสมาชิกในเอกภพสัมพัทธ์</li>
        <li><b>สำหรับบางตัว ($\exists x P(x)$):</b> เป็นจริงเมื่อมีสมาชิกอย่างน้อยหนึ่งตัวที่ทำให้ $P(x)$ เป็นจริง</li>
    </ul>
    <hr>
    <h4>🚫 กฎการนิเสธตัวบ่งปริมาณ</h4>
    <p>• $\sim \forall x P(x) \equiv \exists x \sim P(x)$<br>
       • $\sim \exists x P(x) \equiv \forall x \sim P(x)$</p>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ==================== 07. สรุปสูตรแผ่นเดียว ====================
elif menu == "07. สรุปสูตรแผ่นเดียว (Cheat Sheet)":
    st.markdown(
        '<p class="main-title">📋 07. สรุปสูตรแผ่นเดียว (Cheat Sheet)</p>',
        unsafe_allow_html=True,
    )
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
    <div class="card">
    <h4>💡 หน้ารวมสูตรฉบับพกพา สำหรับเปิดดูทบทวนด่วนขณะทำโจทย์</h4>
    <hr>
    <p><b>1. สมบัติและการสมมูลสำคัญ:</b><br>
    • $P \rightarrow Q \equiv \sim P \vee Q$<br>
    • $\sim(P \wedge Q) \equiv \sim P \vee \sim Q$<br>
    • $\sim(P \vee Q) \equiv \sim P \wedge \sim Q$<br>
    • $P \leftrightarrow Q \equiv (P \rightarrow Q) \wedge (Q \rightarrow P)$</p>
    
    <p><b>2. กฎการอ้างเหตุผล:</b><br>
    • <b>Modus Ponens:</b> $P \rightarrow Q, P \vdash Q$<br>
    • <b>Modus Tollens:</b> $P \rightarrow Q, \sim Q \vdash \sim P$<br>
    • <b>Hypothetical Syllogism:</b> $P \rightarrow Q, Q \rightarrow R \vdash P \rightarrow R$</p>
    
    <p><b>3. นิเสธตัวบ่งปริมาณ:</b><br>
    • $\sim \forall x P(x) \equiv \exists x \sim P(x)$<br>
    • $\sim \exists x P(x) \equiv \forall x \sim P(x)$</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
