from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("8237328737:AAGGmkDfxwSonk5C36Imyl7s5uAJ-jLZfSw")

# =========================
# SYSTEM STATE (PHASE 1)
# =========================
SYSTEM_STATE = {
    "logged_in": False,
    "auto_trade": False,
    "strategy": None,
    "mode": "PAPER"
}

# =========================
# COMMAND HANDLERS
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Algo Trading Bot (Phase 1)\n\n"
        "Available commands:\n"
        "/login\n"
        "/strategy\n"
        "/autotrade_on\n"
        "/autotrade_off\n"
        "/status\n\n"
        "⚠️ Mode: PAPER (No real trades)"
    )

async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    SYSTEM_STATE["logged_in"] = True
    await update.message.reply_text("✅ Logged in successfully (mock login).")

async def strategy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # For now, fixed strategy
    SYSTEM_STATE["strategy"] = "EMA_VWAP"
    await update.message.reply_text(
        "📊 Strategy selected: EMA_VWAP\n"
        "(You can change this later)"
    )

async def autotrade_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not SYSTEM_STATE["logged_in"]:
        await update.message.reply_text("❌ Please /login first.")
        return

    if not SYSTEM_STATE["strategy"]:
        await update.message.reply_text("❌ Please select a /strategy first.")
        return

    SYSTEM_STATE["auto_trade"] = True
    await update.message.reply_text(
        "🚀 Auto Trade ENABLED\n"
        "Mode: PAPER\n"
        "Strategy: EMA_VWAP"
    )

async def autotrade_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    SYSTEM_STATE["auto_trade"] = False
    await update.message.reply_text("🛑 Auto Trade DISABLED (Safe stop).")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "📌 SYSTEM STATUS\n\n"
        f"Logged in: {'✅' if SYSTEM_STATE['logged_in'] else '❌'}\n"
        f"Auto Trade: {'ON ✅' if SYSTEM_STATE['auto_trade'] else 'OFF ❌'}\n"
        f"Strategy: {SYSTEM_STATE['strategy'] or 'Not selected'}\n"
        f"Mode: {SYSTEM_STATE['mode']}"
    )
    await update.message.reply_text(msg)

# =========================
# APP INIT
# =========================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("login", login))
app.add_handler(CommandHandler("strategy", strategy))
app.add_handler(CommandHandler("autotrade_on", autotrade_on))
app.add_handler(CommandHandler("autotrade_off", autotrade_off))
app.add_handler(CommandHandler("status", status))

print("Bot running in PHASE 1 (Control Only)")
app.run_polling()
