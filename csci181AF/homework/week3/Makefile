ifeq ($(OS),Windows_NT)     # is Windows_NT on XP, 2000, 7, Vista, 10...
    TARGET = kofn.exe
else
    TARGET = kofn
endif

all: $(TARGET)

$(TARGET): kofn.cpp
	clang++ -o $(TARGET) -O2 --std=c++2a -Wall -Wextra -Wno-unused-parameter kofn.cpp

clean:
	rm $(TARGET)

.PHONY: clean