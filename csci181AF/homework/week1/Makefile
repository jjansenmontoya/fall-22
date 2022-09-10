ifeq ($(OS),Windows_NT)     # is Windows_NT on XP, 2000, 7, Vista, 10...
    TARGET = swaps.exe
else
    TARGET = swaps
endif

all: $(TARGET)

$(TARGET): swaps.cpp
	clang++ -o $(TARGET) -O2 --std=c++2a -Wall -Wextra swaps.cpp

clean:
	rm $(TARGET)

.PHONY: clean