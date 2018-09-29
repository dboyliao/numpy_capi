BUILD_DIR := build
LIB_DIR := lib
SOURCE := src

.PHONY : clean

$(LIB_DIR)/_libmylib.so : $(BUILD_DIR)/mylib.o
	mkdir -p $(LIB_DIR)
	gcc -shared -o $@ $^

$(BUILD_DIR)/mylib.o : $(SOURCE)/mylib.c
	mkdir -p $(BUILD_DIR)
	gcc -c -fPIC $^ -o $@

clean :
	rm -vrf $(BUILD_DIR) $(LIB_DIR)