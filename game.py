import random
import streamlit as st

# 设置页面标题
st.title("猜数字小游戏 🎮")

# 初始化游戏状态
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.max_attempts = 10
    st.session_state.game_over = False
    st.session_state.win = False

# 显示游戏说明
st.write("我已经想好了一个1到100之间的数字，你有10次机会来猜它。")

# 游戏主逻辑
if not st.session_state.game_over:
    guess = st.number_input(
        "请输入你的猜测",
        min_value=1,
        max_value=100,
        value=st.session_state.get('last_guess', 50)
    )
    
    if st.button("确认猜测"):
        st.session_state.attempts += 1
        st.session_state.last_guess = guess
        
        if guess < st.session_state.secret_number:
            st.write("太小了！")
        elif guess > st.session_state.secret_number:
            st.write("太大了！")
        else:
            st.session_state.game_over = True
            st.session_state.win = True
            st.balloons()
            st.success(f"恭喜你！你用了{st.session_state.attempts}次猜中了数字{st.session_state.secret_number}！")
        
        # 检查是否用完所有尝试次数
        if st.session_state.attempts >= st.session_state.max_attempts and not st.session_state.win:
            st.session_state.game_over = True
            st.error(f"很遗憾，你没有在{st.session_state.max_attempts}次内猜中。正确的数字是{st.session_state.secret_number}。")
        
        # 显示剩余尝试次数
        remaining = st.session_state.max_attempts - st.session_state.attempts
        st.write(f"剩余尝试次数: {remaining}")
else:
    if st.button("再玩一次"):
        # 重置游戏状态
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.win = False
        st.experimental_rerun()

# 显示游戏状态
st.write(f"当前进度: {st.session_state.attempts}次尝试")