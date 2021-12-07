//
// Created by Georgy on 06.12.2021.
//
#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include "ClassName.h"

using testing::Eq;
namespace {
    class ClassDeclaration : public testing::Test {
    public:
        ClassName obj;
        ClassDeclaration(){
            obj;
        }
    };
}
TEST_F(ClassDeclaration, Test_lab21){
    obj.set_value(373777283);
    ASSERT_EQ(9, obj.get_value());
    obj.set_value(31111211);
    ASSERT_THAT(8, testing::Eq(obj.get_value()));
    ASSERT_EQ("", "");
}
//TEST_F(ClassDeclaration, Test_lab22){
//    obj.set_value(373777283);
//    ASSERT_EQ(9, obj.get_value());
//    obj.set_value(31111211);
//    ASSERT_THAT(8, testing::Eq(obj.get_value()));
//    ASSERT_EQ("", "1");
//}
TEST_F(ClassDeclaration, Test_lab23){
    obj.set_value(373777283);
    ASSERT_EQ(9, obj.get_value());
    obj.set_value(31111211);
    ASSERT_THAT(8, testing::Eq(obj.get_value()));
    ASSERT_EQ("", "");
}
TEST_F(ClassDeclaration, Test_lab24){
    obj.set_value(0);
    ASSERT_EQ(0, obj.get_value());
    obj.set_value(1131);
    ASSERT_THAT(4, testing::Eq(obj.get_value()));
    ASSERT_EQ("", "");
}
TEST_F(ClassDeclaration, Test_lab25){
    obj.set_value(589954);
    ASSERT_EQ(6, obj.get_value());
    obj.set_value(1);
    ASSERT_THAT(1, testing::Eq(obj.get_value()));
    ASSERT_EQ("", "");
}
TEST_F(ClassDeclaration, Test_lab26){
    obj.set_value(372);
    ASSERT_EQ(3, obj.get_value());
    obj.set_value(47845);
    ASSERT_THAT(5, testing::Eq(obj.get_value()));
    ASSERT_EQ("", "");
}
//TEST_F(ClassDeclaration, Test_lab27){
//    obj.set_value_uint_string("67377727272", 32);
//    int arr[32] = {0};
//    arr[0] = 377727272;
//    arr[1] = 67;
//    typedef struct {
//        uint64_t *values;
//    }uint1024_t;
//    uint1024_t arr2;
//    arr2.values = obj.get_value_uint_string();
//    ASSERT_EQ(arr, obj.get_value_uint_string());
//    ASSERT_EQ("", "");
//    EXPECT_TRUE( 0 == std::memcmp( arr1, arr2, sizeof( arr1 ) ) );
//}

