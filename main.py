
from utils.indicators import get_full_analysis as fast_analysis
from utils.indicators_failsafe import get_full_analysis as safe_analysis

# Contoh penggunaan
def run_analysis(mode="fast"):
    if mode == "fast":
        report = fast_analysis()
        print("🚀 Fast Analysis Report:", report)
    elif mode == "safe":
        report = safe_analysis()
        print("🛡️ Safe Analysis Report:", report)
    else:
        print("❌ Mode tidak dikenali!")

if __name__ == "__main__":
    run_analysis("fast")  # atau "safe"
