import sys
import traceback

def main():
    try:
        import tictactoe1
    except KeyboardInterrupt:
        print(" Shutdown requested...exiting")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()