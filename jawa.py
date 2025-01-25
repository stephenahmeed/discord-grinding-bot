import os
import asyncio
import discord
from colorama import init, Fore, Style
import time
from datetime import datetime
import pytz  # Untuk menangani zona waktu
import random  # Untuk pemilihan pesan random

init(autoreset=True)

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
black = Fore.LIGHTBLACK_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL
magenta = Fore.LIGHTMAGENTA_EX

def get_timestamp():
    # Menggunakan zona waktu Asia/Jakarta (WIB)
    wib = pytz.timezone('Asia/Jakarta')
    now = datetime.now(wib)
    return f"{blue}[{now.strftime('%H:%M:%S')}]{reset}"

def log_info(message):
    print(f"{get_timestamp()} {white}INFO{reset}    | {message}")

def log_success(message):
    print(f"{get_timestamp()} {green}SUCCESS{reset} | {message}")

def log_warning(message):
    print(f"{get_timestamp()} {yellow}WARNING{reset} | {message}")

def log_error(message):
    print(f"{get_timestamp()} {red}ERROR{reset}   | {message}")

# Banner
def print_banner():
    print(f"\n{blue}▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰{reset}")
    print(f"{white}      Discord Auto Leveling      {reset}")
    print(f"{yellow}         by: Aethereal          {reset}")
    print(f"{blue}▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰{reset}\n")

print_banner()

def load_tokens():
    tokens = []
    try:
        with open('token.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip() and not line.startswith('#'):
                    tokens.append(line.strip())
            if tokens:
                log_success(f"Berhasil memuat {len(tokens)} token dari token.txt")
            return tokens
    except FileNotFoundError:
        log_error("File token.txt tidak ditemukan!")
        log_info("Buat file token.txt dengan format:")
        print(f"{yellow}TOKEN1{reset}")
        print(f"{yellow}TOKEN2{reset}")
        print(f"{yellow}TOKEN3{reset}")
        exit(1)

class AccountConfig:
    def __init__(self, token, channel_id, message_count, message_delay, delete_mode=True):
        self.token = token
        self.channel_id = channel_id
        self.message_count = message_count
        self.message_delay = message_delay
        self.delete_mode = delete_mode

mainMessages = [
    'Just checking in!',
    'Did anyone see the latest episode?',
    'What everyone up to today?',
    'Cant believe its already this late!',
    'Just finished my tasks, finally!',
    'This weather is something else...',
    'Anyone working on something interesting?',
    'Good morning, everyone!',
    'Time for a quick break, anyone else?',
    'Back to the grind.',
    'Anyone have any tips for leveling up faster?',
    'Just got back, what did I miss?',
    'Feeling motivated today!',
    'Lol, thats hilarious!',
    'Totally agree with you.',
    'Thinking about getting some coffee, brb.',
    'Anyone here into coding?',
    'Oh wow, didnt expect that!',
    'Taking things one step at a time.',
    'Almost there!',
    'Lets keep pushing forward!',
    'Just chilling here for a bit.',
    'Anyone have any weekend plans?',
    'Anyone tried that new game yet?',
    'Haha, I know right?',
    'Feels like time is flying by.',
    'Well, thats a surprise!',
    'Just here to chat and relax.',
    'Anyone else feeling productive today?',
    'Im here to keep you all company!',
    'Hope everyones doing well!',
    'Taking a quick break, needed it.',
    'Lets keep this chat alive!',
    'Anyone else here love a good challenge?',
    'Feels good to be part of this community.',
    'Enjoying the vibe here!',
    'Thinking of learning something new.',
    'Random question: Cats or dogs?',
    'Its always nice to chat with you all.',
    'That sounds awesome!',
    'Haha, love the energy here!',
    'Alright, time to focus!',
    'Whats everyone watching these days?',
    'Just a casual hello!',
    'Oops, wrong chat haha.',
    'Wondering if anyone has advice on leveling?',
    'Anyone working late tonight?',
    'Hey, Im back!',
    'Hope I didnt miss too much.',
    'Alright, lets do this!',
    'Trying to stay motivated!',
    'Hows everyone feeling today?',
    'Good vibes only!',
    'Just saw something really cool!'
]

class Main(discord.Client):
    def __init__(self, config):
        super().__init__()
        self.config = config
        
    async def on_ready(self):
        log_success(f"Logged in as {self.user}")
        log_info(f"Mencoba membuka channel...")
        
        channel = self.get_channel(self.config.channel_id)
        
        if not channel:
            log_error(f"Channel tidak ditemukan!")
            await self.close()
            return
            
        log_success(f"Berhasil terhubung ke channel #{channel.name}")
        sent_count = 0

        while sent_count < self.config.message_count:
            # Memilih pesan secara random
            msg = random.choice(mainMessages)
            try:
                sent_message = await channel.send(msg)
                log_success(f"[{self.user}] Pesan {sent_count+1}/{self.config.message_count} terkirim")
                
                if self.config.delete_mode:
                    try:
                        await sent_message.delete()
                        log_info(f"[{self.user}] Pesan {sent_count+1} dihapus")
                    except discord.errors.Forbidden:
                        log_warning(f"[{self.user}] Tidak bisa menghapus pesan (tidak ada izin)")
                    except discord.errors.NotFound:
                        log_warning(f"[{self.user}] Pesan sudah dihapus")
                
                sent_count += 1
                
            except discord.errors.Forbidden as e:
                if "Cannot send messages in a voice channel" in str(e):
                    log_error(f"[{self.user}] Tidak bisa mengirim pesan di voice channel!")
                    await self.close()
                    return
                elif "slowmode" in str(e).lower():
                    log_warning(f"[{self.user}] Channel dalam mode slowmode. Menunggu...")
                    await asyncio.sleep(10)
                    continue
                elif "timeout" in str(e).lower():
                    log_error(f"[{self.user}] Akun sedang dalam timeout!")
                    await self.close()
                    return
                else:
                    log_error(f"[{self.user}] Tidak bisa mengirim pesan! ({str(e)})")
                    await self.close()
                    return
                    
            except discord.errors.HTTPException as e:
                if e.code == 429:  # Rate limit
                    retry_after = e.retry_after
                    log_warning(f"[{self.user}] Rate limit terdeteksi. Menunggu {retry_after} detik...")
                    await asyncio.sleep(retry_after)
                    continue
                else:
                    log_error(f"[{self.user}] Error HTTP: {str(e)}")
                    continue
                    
            except Exception as e:
                log_error(f"[{self.user}] Error tidak dikenal: {str(e)}")
                continue
                
            await asyncio.sleep(self.config.message_delay)

        log_success(f"[{self.user}] Berhasil mengirim {self.config.message_count} pesan")
        await self.close()

def main():
    log_info("Memuat token dari token.txt...")
    tokens = load_tokens()
    
    if not tokens:
        log_error("Tidak ada token yang berhasil dimuat!")
        return

    print(f"\n{white}Pilih Mode Leveling:{reset}")
    print(f"{blue}1. {white}Leveling with Delete Message enable{reset}")
    print(f"{blue}2. {white}Leveling without Delete Message{reset}")
    
    while True:
        try:
            mode = int(input(f"\n{magenta}Pilih mode [1/2]: {reset}"))
            if mode in [1, 2]:
                break
            print(f"{red}Pilihan tidak valid! Pilih 1 atau 2.{reset}")
        except ValueError:
            print(f"{red}Input tidak valid! Masukkan angka 1 atau 2.{reset}")
    
    delete_mode = mode == 1
    
    channel_id = int(input(f"{magenta}Masukkan Channel ID: {reset}"))
    message_count = int(input(f"{magenta}Berapa banyak pesan yang akan dikirim: {reset}"))
    message_delay = int(input(f"{magenta}Delay antara setiap pesan (dalam detik): {reset}"))
    
    accounts = []
    for token in tokens:
        accounts.append(AccountConfig(token, channel_id, message_count, message_delay, delete_mode))
    
    # Menjalankan akun satu per satu
    for i, config in enumerate(accounts, 1):
        log_info(f"Menjalankan akun {i} dari {len(accounts)}...")
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            client = Main(config)
            client.run(config.token, bot=False)
        except discord.LoginFailure:
            log_error(f"Token tidak valid atau expired!")
        except discord.PrivilegedIntentsRequired:
            log_error(f"Intents tidak diizinkan!")
        except Exception as e:
            log_error(f"Error: {str(e)}")
        finally:
            try:
                loop.close()
            except:
                pass
            
        if i < len(accounts):
            log_info(f"Menunggu 5 detik sebelum menjalankan akun berikutnya...")
            time.sleep(5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log_warning("Program dihentikan oleh user")
    except Exception as e:
        log_error(f"Terjadi error: {e}")
