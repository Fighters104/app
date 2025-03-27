import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# アプリのタイトル
st.title('企業の株価チャート')

# 企業名を入力するテキストボックス
company_name = st.text_input('企業のティッカーシンボルを入力してください（例: AAPL GOOGL TSLA）')

if company_name:
    try:
        # 企業名からティッカーシンボルを取得
        ticker = yf.Ticker(company_name)
        
        # 株価データを取得（過去1年分）
        data = ticker.history(period="1y")
        
        # 株価チャートの作成
        fig = go.Figure(data=[go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            name=company_name
        )])

        # チャートのレイアウト設定
        fig.update_layout(
            title=f'{company_name}の株価チャート',
            xaxis_title='日付',
            yaxis_title='株価',
            xaxis_rangeslider_visible=False
        )

        # チャートを表示
        st.plotly_chart(fig)

    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
