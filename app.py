import streamlit as st
import random

# ====================
# 1. 頁面設定
# ====================
st.set_page_config(page_title="慾望輪盤：攻守交換版", page_icon="🔥", layout="centered")

# ====================
# 2. CSS 美化
# ====================
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 3.5em;
        font-size: 20px !important;
        font-weight: bold;
        border-radius: 12px;
    }
    .big-text {
        font-size: 22px !important;
        line-height: 1.6;
        font-weight: 500;
        color: #ffffff;
    }
    .card-box {
        padding: 25px;
        border-radius: 15px;
        background-color: #262730;
        border: 2px solid #ff4b4b;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .punish-box {
        border-color: #ff0000 !important;
        background-color: #3d0000 !important;
    }
    .role-indicator {
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 10px;
    }
    .dom-role { background-color: #4b0082; color: white; border: 1px solid #8a2be2; }
    .sub-role { background-color: #2e2e2e; color: #aaaaaa; border: 1px solid #555; }
    .highlight-dom { color: #ff88ff; font-weight: bold; text-decoration: underline; }
    .highlight-sub { color: #88ccff; font-weight: bold; text-decoration: underline; }
    </style>
    """, unsafe_allow_html=True)

# ====================
# 3. 遊戲資料庫
# ====================
levels = {
    'S': [
        "S1: 嗅覺誘惑 - {sub}閉眼，{dom}把遙控跳蛋塞進你騷逼裡開震，同時舔你耳朵說「等下{dom}要操到你噴水求饒」。",
        "S2: 溫度反差 - 用冰塊磨{sub}陰蒂/龜頭，再用熱蠟滴在奶頭和大腿根，讓{sub}爽到哭著叫爸爸。",
        "S3: 沉默的觸摸 - 10分鐘不准出聲，{dom}用指甲刮{sub}屁眼和會陰，誰先浪叫誰就是欠操的母狗。",
        "S4: 濕度評測 - {sub}用騷逼/硬雞巴磨{dom}，直到{dom}說「夠濕了，準備被操爛」為止。",
        "S5: 呼吸控制 - {dom}掐著{sub}脖子狂吻，讓你喘不過氣，臉紅到翻白眼求{dom}幹你。",
        "S6: 專屬氣味 - 戴眼罩的{sub}用舌頭舔{dom}的奶頭、腋下、屁眼，猜出3個最騷的地方才准停。",
        "S7: 專注的口慾 - {sub}給{dom}站好不准動，{dom}舔你奶頭和會陰5分鐘，就是不碰你下面，讓你急到滴水。",
        "S8: 四肢綑綁 - 用手銬把{sub}綁成M字腿騷逼大開，{dom}要慢慢欣賞你發浪。",
        "S9: 羽毛輕拂 - 用羽毛刷{sub}腳底、奶頭、陰囊/陰唇3分鐘，讓你癢到扭腰求{dom}直接插進來。",
        "S10: 情慾繪畫 - 用潤滑液在{sub}身上寫「公用肉便器」「操爛我」「{dom}的專屬雞巴套」，錯一個就用鞭子抽奶頭。",
        "S11: 內衣透視 - 穿開檔情趣內衣+乳夾，{dom}隔著布料用遙控跳蛋震你陰蒂/龜頭3分鐘，讓你浪叫求脫。",
        "S12: 慾望脫線 - 穿開檔內褲，{dom}用手指慢慢掰開{sub}陰唇/包皮，拉長3分鐘，讓騷水流滿地。"
    ],
    'D': [
        "D1: 口頭服從 - {sub}跪下叫十聲「{dom}操我」，然後舔{dom}屁眼或腳趾，像條母狗一樣。",
        "D2: 等待的懲罰 - 快射/噴時{dom}立刻停，逼{sub}在60秒內哭著說「{dom}我錯了，請操爛我的騷逼/雞巴」。",
        "D3: 姿勢鎖定 - 維持狗爬式或M字腿，{dom}用假屌或電擊貼片慢慢玩{sub}騷穴/雞巴。",
        "D4: 發號施令 - 不碰{sub}下面，只用最髒的話命令你自己插肛塞或摳逼，邊做邊說「我好欠操」。",
        "D5: 雙重限制 - {dom}戴眼罩，塞{sub}口球，只靠你扭屁股的程度決定用多大力玩乳夾。",
        "D6: 慾望懲罰 - 接下來10次求饒就用鞭子抽{sub}屁股或滴蠟在奶頭，讓你記住誰是主人。",
        "D7: 完全靜止 - {sub}雙手舉高過頭不准動，{dom}滴蠟滿你奶頭和大腿內側。",
        "D8: 語音剝奪 - 塞口球只准流口水扭逼，表示想被{dom}操爛。",
        "D9: 口頭控制 - {sub}雙手舉高，{dom}命令「把腿張到最大」「翹屁股求插」「叫給{dom}聽」。",
        "D10: 高潮懸崖 - 計時10分鐘，誰先射誰就戴鎖精環+肛塞當一晚肉便器。"
    ],
    'T': [
        "T1: 無手挑戰 - 把跳蛋塞進{sub}騷逼/貼在雞巴上開最大檔5分鐘，{dom}只舔其他地方，讓你爽到發瘋。",
        "T2: 鎖精耐久 - 戴鎖精環+肛塞，{dom}用飛機杯或假屌磨你，就是不讓你射，讓{sub}哭著求饒。",
        "T3: 主人與奴僕 - {dom}戴假屌，{sub}戴眼罩+手銬+口球，跪著用身體磨求{dom}插進去。",
        "T4: 八抓椅極限 - 把{sub}綁在八抓椅上，用跳蛋+假屌+乳夾+電擊貼片同時操爛你。",
        "T5: 振動轉移 - 先用跳蛋震{sub}陰蒂/龜頭3分鐘，再轉移到肛塞，前後一起爽到你失禁。",
        "T6: 飛機杯的試煉 - {sub}自己用飛機杯，{dom}隨時抽走或用鞭子抽，讓你哭著求{dom}讓你射。",
        "T7: 手銬解鎖 - 手銬鎖{sub}，把鑰匙塞{dom}屁眼，讓你用舌頭挖出來舔乾淨。",
        "T8: 假屌感官遊走 - 用假屌頭磨{sub}奶頭、陰蒂、屁眼，就是不插進去，讓你急到發浪。",
        "T9: 道具三明治 - 同時用手、口、跳蛋、假屌、肛塞操{sub}三穴，直到你崩潰噴水。",
        "T10: 雙重振動 - 前面塞跳蛋，後面塞震動肛塞，奶頭夾乳夾，同時開最大檔。",
        "T11: 自慰棒引導 - {dom}用自慰棒狂插{sub}騷逼/屁眼，你必須同時用假屌回操{dom}。",
        "T12: 自慰棒挑戰 - 戴眼罩的{sub}用自慰棒找{dom}身上最敏感的點，找錯就電擊奶頭。",
        "T13: 電玩模式 - 用手機App控制跳蛋+肛塞+電擊貼片，{sub}猜錯模式就加10秒最高檔。"
    ],
    'P': [
        "P1: 核心三連擊 (60秒) - 20秒狂野女上操到子宮 → 20秒背入撞爛屁股 → 20秒側躺插到翻白眼。",
        "P2: 體力流動 (90秒) - 30秒站立後入抬腿深插 → 30秒抱起來操到腿軟 → 30秒頂到最深處。",
        "P3: 視覺衝擊 (120秒) - 40秒面對鏡子看自己被操到哭 → 40秒單膝跪深喉到吐 → 40秒正面狂吻猛幹。",
        "P4: 單點壓力測試 - 選高難姿勢維持3分鐘，{dom}只用假屌頭狂攻G點或前列腺，讓{sub}噴個不停。",
        "P5: 核心位移 (150秒) - 50秒後入猛幹到子宮 → 50秒抱腿式抬高狂頂 → 50秒側躺鎖喉插爛。",
        "P6: 鏡面反射 - 面對鏡子做傳教士，強制{sub}看著自己被操到失神的騷樣3分鐘。",
        "P7: 橋式懸空 - {sub}橋式翹臀，{dom}從下方用假屌狂頂到你腿抖4分鐘。",
        "P8: 69變形 - 側躺69，輪流深喉到噁心乾嘔5分鐘。",
        "P9: 蓮花深融 - 面對面坐姿，{dom}控制深度猛撞到子宮，{sub}只能抱緊哭喊4分鐘。",
        "P10: 牆壁征服 - {sub}靠牆抬雙腿，{dom}站著狂插到你腿軟站不住5分鐘。"
    ],
    'X': [
        "X1: 核心節奏 - 不准出聲，只用眼神呼吸同步猛幹，錯一次停30秒+鞭打{sub}奶頭10下。",
        "X2: 失敗的代價 - 180秒內必須讓{sub}噴/射，失敗就戴口球+鎖精環+肛塞當一晚肉便器。",
        "X3: 共享邊緣極限 - 緊密連結5分鐘內同時到邊緣，誰先射誰就當晚被綁起來操到天亮。",
        "X4: 凍結與羞辱 - {dom}有3次凍結權，每次120秒，{sub}動一下就電擊奶頭或陰蒂。",
        "X5: 恒定高難度 - 維持極難姿勢5分鐘狂操，姿勢崩就滴蠟+鞭打重來。",
        "X6: 高潮後的服從 - 高潮後30秒內說出最變態的幻想，否則{dom}再操到你下一次噴。",
        "X7: 無手高潮的時限 - 5分鐘內只用身體摩擦+乳夾讓{sub}射，失敗就戴鎖精環過夜。",
        "X8: 累積慾望的屈服 - 6次邊緣後哭著說5句「我是{dom}的專屬肉便器」才准射。",
        "X9: 赤裸告白與主導 - 高潮前10秒倒數，大喊最髒的慾望，否則停止並鞭打屁股。",
        "X10: 連續三次的風險 - 12分鐘內讓{sub}連續高潮3次，失敗就當晚三穴完全開放。",
        "X11: 肛塞鎖喉狂插 - {sub}戴最大號肛塞，{dom}鎖喉深插10分鐘，前後一起操到你失禁。",
        "X12: 乳夾電擊連擊 - 乳夾+電擊貼片開最大檔，{dom}狂幹到{sub}噴滿床。",
        "X13: 蠟燭滴滿全身 - 邊狂插邊滴蠟滿奶頭、陰蒂、屁股，讓{sub}痛到爽到哭。",
        "X14: 口球深喉懲罰 - 塞口球後強迫深喉假屌5分鐘，同時遙控跳蛋震到你崩潰。",
        "X15: 終極性奴之夜 - 綁在八抓椅上，用所有道具輪番操{sub}三穴到天亮，無條件當{dom}的專屬肉便器。"
    ]
}

punishments = [
    "懲罰1：跪舔屁眼 - {sub}跪下舔{dom}屁眼60秒，邊舔邊哭說「謝謝{dom}讓賤貨舔」。",
    "懲罰2：公開自慰 - 當場摳逼/打手槍到邊緣不准射，{dom}全程看你發浪。",
    "懲罰3：乳夾+鞭打 - {sub}戴乳夾2分鐘，被鞭子抽屁股20下，每下叫「謝謝{dom}」。",
    "懲罰4：肛塞過夜 - {sub}塞最大號肛塞過夜，明天早上{dom}才拔，讓你記住誰是主人。",
    "懲罰5：鏡前辱罵 - 面對鏡子說30句「我是賤貨」「操爛我的騷逼」之類的髒話。",
    "懲罰6：蠟燭+電擊 - 滴蠟10滴後電擊奶頭3次，讓{sub}痛到噴水。",
    "懲罰7：口球流口水 - {sub}戴口球3分鐘，只能流口水呻吟求{dom}操你。",
    "懲罰8：強制高潮 - 被操到強制高潮5次，中間不准休息。",
    "懲罰9：三穴開放 - 當場嘴巴、騷逼、屁眼同時被道具塞滿5分鐘。",
    "懲罰10：一晚肉便器 - 當晚完全淪為{dom}的專屬肉便器，任操任玩到天亮。"
]

level_order = ['S', 'D', 'T', 'P', 'X']
level_names = {
    'S': "感官 (Sensory)", 
    'D': "羞辱 (Discipline)", 
    'T': "道具 (Toys)", 
    'P': "體位 (Position)", 
    'X': "極限 (Extreme)"
}
scores_map = {'S':1, 'D':2, 'T':3, 'P':4, 'X':7}

# ====================
# 4. 遊戲邏輯核心
# ====================
# 初始化狀態
if 'p1_score' not in st.session_state:
    st.session_state.p1_score = 0
if 'p2_score' not in st.session_state:
    st.session_state.p2_score = 0
if 'round' not in st.session_state:
    st.session_state.round = 1
if 'game_phase' not in st.session_state:
    st.session_state.game_phase = 'ready'
if 'level_index' not in st.session_state:
    st.session_state.level_index = 0
if 'turn_owner' not in st.session_state:
    st.session_state.turn_owner = 0 # 0: P1攻, 1: P2攻

if 'current_card' not in st.session_state:
    st.session_state.current_card = ""
if 'punishment_text' not in st.session_state:
    st.session_state.punishment_text = ""

# 側邊欄
with st.sidebar:
    st.title("⚙️ 玩家設定")
    p1_name_input = st.text_input("玩家 1 名字", value="老公")
    p2_name_input = st.text_input("玩家 2 名字", value="老婆")
    threshold = st.number_input("高潮閾值 (分數)", value=50, step=10)
    
    st.divider()
    st.info("模式：攻守交換 + 循序漸進\n\n每回合交換攻受角色，失敗會退回上一階層。")
    
    if st.button("🔄 重置所有進度"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

# 確定當前角色的名字
# turn_owner = 0 -> P1是攻 (Dom), P2是受 (Sub)
# turn_owner = 1 -> P2是攻 (Dom), P1是受 (Sub)
if st.session_state.turn_owner == 0:
    current_dom_name = p1_name_input
    current_sub_name = p2_name_input
else:
    current_dom_name = p2_name_input
    current_sub_name = p1_name_input

# 輔助函式：替換名字 (加上顏色)
def replace_names(text, dom, sub):
    t = text
    t = t.replace("老子", dom).replace("主人", dom)
    t = t.replace("你", sub).replace("賤貨", sub).replace("肉便器", sub)
    # 使用 f-string 注入 HTML 顏色
    t = t.format(
        dom=f"<span class='highlight-dom'>{dom}</span>", 
        sub=f"<span class='highlight-sub'>{sub}</span>"
    )
    return t

# 標題區
st.title("🔥🔥 慾望輪盤：攻守交換版")

# 分數與進度顯示
current_lvl_key = level_order[st.session_state.level_index]
current_lvl_name = level_names[current_lvl_key]

c1, c2, c3 = st.columns([2, 2, 2])
c1.metric(p1_name_input, f"{st.session_state.p1_score}", delta="玩家 1")
c2.metric(p2_name_input, f"{st.session_state.p2_score}", delta="玩家 2")
c3.metric("目前強度", f"{current_lvl_key} - {st.session_state.level_index + 1}/5", delta=current_lvl_name)

# 進度條
total_score = st.session_state.p1_score + st.session_state.p2_score
st.progress(min(total_score / (threshold * 1.5), 1.0)) # 視覺用，兩個人加起來的熱度

st.divider()

# 勝利判斷
if st.session_state.p1_score >= threshold or st.session_state.p2_score >= threshold:
    winner = p1_name_input if st.session_state.p1_score > st.session_state.p2_score else p2_name_input
    st.balloons()
    st.error(f"🏆 遊戲結束！{winner} 的慾望更勝一籌！")
    
    # 決定誰是終極輸家 (分數低者，或自訂邏輯)
    loser = p2_name_input if winner == p1_name_input else p1_name_input
    
    st.markdown(f"""
    <div class="card-box punish-box">
        <h3 style="color:white; text-align:center;">🔥 終極高潮時刻 🔥</h3>
        <p class="big-text" style="text-align:center;">
        今晚 <b>{loser}</b> 必須無條件服從 <b>{winner}</b>，直到天亮！
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("再來一局 (重置)"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
    st.stop()

# 主要遊戲區
placeholder = st.empty()

with placeholder.container():
    # 顯示當前攻守狀態
    role_html = f"""
    <div style="display: flex; gap: 10px; margin-bottom: 20px;">
        <div style="flex: 1;" class="role-indicator dom-role">👑 攻方 (Dom)：{current_dom_name}</div>
        <div style="flex: 1;" class="role-indicator sub-role">⛓️ 受方 (Sub)：{current_sub_name}</div>
    </div>
    """
    st.markdown(role_html, unsafe_allow_html=True)

    # 階段 1: 準備抽卡
    if st.session_state.game_phase == 'ready':
        st.info(f"第 {st.session_state.round} 回合 | 強度：{current_lvl_name}")
        
        btn_label = f"🔥 {current_dom_name} 抽取指令 (對 {current_sub_name})"
        
        if st.button(btn_label, type="primary"):
            raw_card = random.choice(levels[current_lvl_key])
            st.session_state.current_card = raw_card
            st.session_state.game_phase = 'action'
            st.rerun()

    # 階段 2: 顯示指令 (自動換名)
    elif st.session_state.game_phase == 'action':
        pts = scores_map[current_lvl_key]
        color_map = {'S': '🟣', 'D': '🟡', 'T': '🟠', 'P': '🟢', 'X': '🔴'}
        
        # 替換名字
        display_text = replace_names(st.session_state.current_card, current_dom_name, current_sub_name)
        
        st.subheader(f"{color_map[current_lvl_key]} Level {current_lvl_key} (+{pts}分)")
        
        st.markdown(f"""
        <div class="card-box">
            <p class="big-text">{display_text}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_yes, col_no = st.columns(2)
        
        # 成功
        if col_yes.button("✅ 執行成功 (換手+晉級)", type="primary"):
            # 誰是攻方，誰就加分 (或雙方都加，這裡設定攻方加分)
            if st.session_state.turn_owner == 0:
                st.session_state.p1_score += pts
            else:
                st.session_state.p2_score += pts
            
            st.session_state.round += 1
            
            # 升級
            if st.session_state.level_index < 4:
                st.session_state.level_index += 1
            
            # 交換攻守
            st.session_state.turn_owner = 1 - st.session_state.turn_owner
            st.session_state.game_phase = 'ready'
            st.rerun()
            
        # 失敗
        if col_no.button("❌ 拒絕/失敗 (懲罰+退階)"):
            punish_raw = random.choice(punishments)
            st.session_state.punishment_text = punish_raw
            st.session_state.game_phase = 'punish'
            st.rerun()

    # 階段 3: 懲罰
    elif st.session_state.game_phase == 'punish':
        st.error(f"⚠️ {current_sub_name} 執行失敗！接受懲罰！")
        
        # 懲罰文字通常是 {sub} 被處罰，所以名字邏輯一樣
        punish_display = replace_names(st.session_state.punishment_text, current_dom_name, current_sub_name)
        
        st.markdown(f"""
        <div class="card-box punish-box">
            <p class="big-text">{punish_display}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("😭 接受懲罰 (換手)"):
            st.session_state.round += 1
            
            # 降級
            if st.session_state.level_index > 0:
                st.session_state.level_index -= 1
            
            # 懲罰結束後，依然要交換攻守
            st.session_state.turn_owner = 1 - st.session_state.turn_owner
            st.session_state.game_phase = 'ready'
            st.rerun()
