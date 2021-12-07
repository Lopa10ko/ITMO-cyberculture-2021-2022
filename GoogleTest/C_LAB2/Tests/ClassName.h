//
// Created by Georgy on 06.12.2021.
//

#ifndef C_LAB2_CLASSNAME_H
#define C_LAB2_CLASSNAME_H


class ClassName{
public:
    typedef struct {
        uint64_t *values;
    }uint1024_t;
    int value;
    uint1024_t string_uint;
    static int get_length_uint64(int value) {int cnt = 0; while(value>0){value /= 10; cnt += 1;} return cnt;}
    int get_value() const {
        return value;
    }
    void set_value(int value) {
        ClassName::value = get_length_uint64(value);
    }
    uint1024_t from_string(const char * string, int base) {
        uint1024_t num;
        num.values = static_cast<uint64_t *>(malloc(base * sizeof(uint64_t)));
        for (int i = 0; i < base; i++) {num.values[i] = 0;}
        // if strlen/9 > base -> warning
        unsigned long str_size = strlen(string);
        int power = 0, lim = 3;
        for (unsigned int i = str_size; i > 0; i--){
            num.values[(str_size - i) / lim] += (string[i - 1] - '0') * pow(10, ++power - 1);
            if(power == lim) {power = 0;}
        }
        return num;
    }
    uint1024_t get_value_uint_string() const {
        return string_uint;
    }
    void set_value_uint_string(const char * value, int base) {
        ClassName::string_uint = from_string(value, base);
    }
};


#endif //C_LAB2_CLASSNAME_H
