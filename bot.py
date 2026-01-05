from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = "8237328737:AAGGmkDfxwSonk5C36Imyl7s5uAJ-jLZfSw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi 👋\n\n"
        "Available commands:\n"
        "/notes - Get notes PDF\n"
        "/syllabus - Get syllabus PDF"
    )

async def notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pdf_path = "pdfs/notes.pdf"

    if not os.path.exists(pdf_path):
        await update.message.reply_text("❌ Notes PDF not found.")
        return

    await update.message.reply_document(
        document=open(pdf_path, "rb"),
        filename="Notes.pdf",
        caption="📘 Your Notes PDF"
    )

async def syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pdf_path = "pdfs/syllabus.pdf"

    if not os.path.exists(pdf_path):
        await update.message.reply_text("❌ Syllabus PDF not found.")
        return

    await update.message.reply_document(
        document=open(pdf_path, "rb"),
        filename="Syllabus.pdf",
        caption="📄 Syllabus PDF"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("notes", notes))
app.add_handler(CommandHandler("syllabus", syllabus))

print("Bot is running...")
app.run_polling()

