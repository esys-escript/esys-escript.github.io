
void blockpapi_addEvent(int event, char *description);
void blockpapi_start();
void blockpapi_stop();
void blockpapi_writeReport();
long long *blockpapi_getValues();
void blockpapi_writeSystemInfo();

/* These define NATV_the event codes for all the native events listed by native_avail */

#define NATV_ALAT_CAPACITY_MISS_ALL	0x40000000
#define NATV_ALAT_CAPACITY_MISS_FP	0x40000001
#define NATV_ALAT_CAPACITY_MISS_INT	0x40000002
#define NATV_BACK_END_BUBBLE_ALL	0x40000003
#define NATV_BACK_END_BUBBLE_FE	0x40000004
#define NATV_BACK_END_BUBBLE_L1D_FPU_RSE	0x40000005
#define NATV_BE_BR_MISPRED_DETAIL_ANY	0x40000006
#define NATV_BE_BR_MISPRED_DETAIL_PFS	0x40000007
#define NATV_BE_BR_MISPRED_DETAIL_ROT	0x40000008
#define NATV_BE_BR_MISPRED_DETAIL_STG	0x40000009
#define NATV_BE_EXE_BUBBLE_ALL	0x4000000a
#define NATV_BE_EXE_BUBBLE_ARCR	0x4000000b
#define NATV_BE_EXE_BUBBLE_ARCR_PR_CANCEL_BANK	0x4000000c
#define NATV_BE_EXE_BUBBLE_BANK_SWITCH	0x4000000d
#define NATV_BE_EXE_BUBBLE_CANCEL	0x4000000e
#define NATV_BE_EXE_BUBBLE_FRALL	0x4000000f
#define NATV_BE_EXE_BUBBLE_GRALL	0x40000010
#define NATV_BE_EXE_BUBBLE_GRGR	0x40000011
#define NATV_BE_EXE_BUBBLE_PR	0x40000012
#define NATV_BE_FLUSH_BUBBLE_ALL	0x40000013
#define NATV_BE_FLUSH_BUBBLE_BRU	0x40000014
#define NATV_BE_FLUSH_BUBBLE_XPN	0x40000015
#define NATV_BE_L1D_FPU_BUBBLE_ALL	0x40000016
#define NATV_BE_L1D_FPU_BUBBLE_FPU	0x40000017
#define NATV_BE_L1D_FPU_BUBBLE_L1D	0x40000018
#define NATV_BE_L1D_FPU_BUBBLE_L1D_DCS	0x40000019
#define NATV_BE_L1D_FPU_BUBBLE_L1D_DCURECIR	0x4000001a
#define NATV_BE_L1D_FPU_BUBBLE_L1D_FILLCONF	0x4000001b
#define NATV_BE_L1D_FPU_BUBBLE_L1D_FULLSTBUF	0x4000001c
#define NATV_BE_L1D_FPU_BUBBLE_L1D_HPW	0x4000001d
#define NATV_BE_L1D_FPU_BUBBLE_L1D_L2BPRESS	0x4000001e
#define NATV_BE_L1D_FPU_BUBBLE_L1D_LDCHK	0x4000001f
#define NATV_BE_L1D_FPU_BUBBLE_L1D_LDCONF	0x40000020
#define NATV_BE_L1D_FPU_BUBBLE_L1D_NAT	0x40000021
#define NATV_BE_L1D_FPU_BUBBLE_L1D_NATCONF	0x40000022
#define NATV_BE_L1D_FPU_BUBBLE_L1D_STBUFRECIR	0x40000023
#define NATV_BE_L1D_FPU_BUBBLE_L1D_TLB	0x40000024
#define NATV_BE_LOST_BW_DUE_TO_FE_ALL	0x40000025
#define NATV_BE_LOST_BW_DUE_TO_FE_BI	0x40000026
#define NATV_BE_LOST_BW_DUE_TO_FE_BRQ	0x40000027
#define NATV_BE_LOST_BW_DUE_TO_FE_BR_ILOCK	0x40000028
#define NATV_BE_LOST_BW_DUE_TO_FE_BUBBLE	0x40000029
#define NATV_BE_LOST_BW_DUE_TO_FE_FEFLUSH	0x4000002a
#define NATV_BE_LOST_BW_DUE_TO_FE_FILL_RECIRC	0x4000002b
#define NATV_BE_LOST_BW_DUE_TO_FE_IBFULL	0x4000002c
#define NATV_BE_LOST_BW_DUE_TO_FE_IMISS	0x4000002d
#define NATV_BE_LOST_BW_DUE_TO_FE_PLP	0x4000002e
#define NATV_BE_LOST_BW_DUE_TO_FE_TLBMISS	0x4000002f
#define NATV_BE_LOST_BW_DUE_TO_FE_UNREACHED	0x40000030
#define NATV_BE_RSE_BUBBLE_ALL	0x40000031
#define NATV_BE_RSE_BUBBLE_AR_DEP	0x40000032
#define NATV_BE_RSE_BUBBLE_BANK_SWITCH	0x40000033
#define NATV_BE_RSE_BUBBLE_LOADRS	0x40000034
#define NATV_BE_RSE_BUBBLE_OVERFLOW	0x40000035
#define NATV_BE_RSE_BUBBLE_UNDERFLOW	0x40000036
#define NATV_BRANCH_EVENT	0x40000037
#define NATV_BR_MISPRED_DETAIL_ALL_ALL_PRED	0x40000038
#define NATV_BR_MISPRED_DETAIL_ALL_CORRECT_PRED	0x40000039
#define NATV_BR_MISPRED_DETAIL_ALL_WRONG_PATH	0x4000003a
#define NATV_BR_MISPRED_DETAIL_ALL_WRONG_TARGET	0x4000003b
#define NATV_BR_MISPRED_DETAIL_IPREL_ALL_PRED	0x4000003c
#define NATV_BR_MISPRED_DETAIL_IPREL_CORRECT_PRED	0x4000003d
#define NATV_BR_MISPRED_DETAIL_IPREL_WRONG_PATH	0x4000003e
#define NATV_BR_MISPRED_DETAIL_IPREL_WRONG_TARGET	0x4000003f
#define NATV_BR_MISPRED_DETAIL_NTRETIND_ALL_PRED	0x40000040
#define NATV_BR_MISPRED_DETAIL_NTRETIND_CORRECT_PRED	0x40000041
#define NATV_BR_MISPRED_DETAIL_NTRETIND_WRONG_PATH	0x40000042
#define NATV_BR_MISPRED_DETAIL_NTRETIND_WRONG_TARGET	0x40000043
#define NATV_BR_MISPRED_DETAIL_RETURN_ALL_PRED	0x40000044
#define NATV_BR_MISPRED_DETAIL_RETURN_CORRECT_PRED	0x40000045
#define NATV_BR_MISPRED_DETAIL_RETURN_WRONG_PATH	0x40000046
#define NATV_BR_MISPRED_DETAIL_RETURN_WRONG_TARGET	0x40000047
#define NATV_BR_MISPRED_DETAIL2_ALL_ALL_UNKNOWN_PRED	0x40000048
#define NATV_BR_MISPRED_DETAIL2_ALL_UNKNOWN_PATH_CORRECT_PRED	0x40000049
#define NATV_BR_MISPRED_DETAIL2_ALL_UNKNOWN_PATH_WRONG_PATH	0x4000004a
#define NATV_BR_MISPRED_DETAIL2_IPREL_ALL_UNKNOWN_PRED	0x4000004b
#define NATV_BR_MISPRED_DETAIL2_IPREL_UNKNOWN_PATH_CORRECT_PRED	0x4000004c
#define NATV_BR_MISPRED_DETAIL2_IPREL_UNKNOWN_PATH_WRONG_PATH	0x4000004d
#define NATV_BR_MISPRED_DETAIL2_NRETIND_ALL_UNKNOWN_PRED	0x4000004e
#define NATV_BR_MISPRED_DETAIL2_NRETIND_UNKNOWN_PATH_CORRECT_PRED	0x4000004f
#define NATV_BR_MISPRED_DETAIL2_NRETIND_UNKNOWN_PATH_WRONG_PATH	0x40000050
#define NATV_BR_MISPRED_DETAIL2_RETURN_ALL_UNKNOWN_PRED	0x40000051
#define NATV_BR_MISPRED_DETAIL2_RETURN_UNKNOWN_PATH_CORRECT_PRED	0x40000052
#define NATV_BR_MISPRED_DETAIL2_RETURN_UNKNOWN_PATH_WRONG_PATH	0x40000053
#define NATV_BR_PATH_PRED_ALL_MISPRED_NOTTAKEN	0x40000054
#define NATV_BR_PATH_PRED_ALL_MISPRED_TAKEN	0x40000055
#define NATV_BR_PATH_PRED_ALL_OKPRED_NOTTAKEN	0x40000056
#define NATV_BR_PATH_PRED_ALL_OKPRED_TAKEN	0x40000057
#define NATV_BR_PATH_PRED_IPREL_MISPRED_NOTTAKEN	0x40000058
#define NATV_BR_PATH_PRED_IPREL_MISPRED_TAKEN	0x40000059
#define NATV_BR_PATH_PRED_IPREL_OKPRED_NOTTAKEN	0x4000005a
#define NATV_BR_PATH_PRED_IPREL_OKPRED_TAKEN	0x4000005b
#define NATV_BR_PATH_PRED_NRETIND_MISPRED_NOTTAKEN	0x4000005c
#define NATV_BR_PATH_PRED_NRETIND_MISPRED_TAKEN	0x4000005d
#define NATV_BR_PATH_PRED_NRETIND_OKPRED_NOTTAKEN	0x4000005e
#define NATV_BR_PATH_PRED_NRETIND_OKPRED_TAKEN	0x4000005f
#define NATV_BR_PATH_PRED_RETURN_MISPRED_NOTTAKEN	0x40000060
#define NATV_BR_PATH_PRED_RETURN_MISPRED_TAKEN	0x40000061
#define NATV_BR_PATH_PRED_RETURN_OKPRED_NOTTAKEN	0x40000062
#define NATV_BR_PATH_PRED_RETURN_OKPRED_TAKEN	0x40000063
#define NATV_BR_PATH_PRED2_ALL_UNKNOWNPRED_NOTTAKEN	0x40000064
#define NATV_BR_PATH_PRED2_ALL_UNKNOWNPRED_TAKEN	0x40000065
#define NATV_BR_PATH_PRED2_IPREL_UNKNOWNPRED_NOTTAKEN	0x40000066
#define NATV_BR_PATH_PRED2_IPREL_UNKNOWNPRED_TAKEN	0x40000067
#define NATV_BR_PATH_PRED2_NRETIND_UNKNOWNPRED_NOTTAKEN	0x40000068
#define NATV_BR_PATH_PRED2_NRETIND_UNKNOWNPRED_TAKEN	0x40000069
#define NATV_BR_PATH_PRED2_RETURN_UNKNOWNPRED_NOTTAKEN	0x4000006a
#define NATV_BR_PATH_PRED2_RETURN_UNKNOWNPRED_TAKEN	0x4000006b
#define NATV_BUS_ALL_ANY	0x4000006c
#define NATV_BUS_ALL_IO	0x4000006d
#define NATV_BUS_ALL_SELF	0x4000006e
#define NATV_BUS_BACKSNP_REQ_THIS	0x4000006f
#define NATV_BUS_BRQ_LIVE_REQ_HI	0x40000070
#define NATV_BUS_BRQ_LIVE_REQ_LO	0x40000071
#define NATV_BUS_BRQ_REQ_INSERTED	0x40000072
#define NATV_BUS_DATA_CYCLE	0x40000073
#define NATV_BUS_HITM	0x40000074
#define NATV_BUS_IO_ANY	0x40000075
#define NATV_BUS_IO_IO	0x40000076
#define NATV_BUS_IO_SELF	0x40000077
#define NATV_BUS_IOQ_LIVE_REQ_HI	0x40000078
#define NATV_BUS_IOQ_LIVE_REQ_LO	0x40000079
#define NATV_BUS_LOCK_ANY	0x4000007a
#define NATV_BUS_LOCK_SELF	0x4000007b
#define NATV_BUS_MEMORY_ALL_ANY	0x4000007c
#define NATV_BUS_MEMORY_ALL_IO	0x4000007d
#define NATV_BUS_MEMORY_ALL_SELF	0x4000007e
#define NATV_BUS_MEMORY_EQ_128BYTE_ANY	0x4000007f
#define NATV_BUS_MEMORY_EQ_128BYTE_IO	0x40000080
#define NATV_BUS_MEMORY_EQ_128BYTE_SELF	0x40000081
#define NATV_BUS_MEMORY_LT_128BYTE_ANY	0x40000082
#define NATV_BUS_MEMORY_LT_128BYTE_IO	0x40000083
#define NATV_BUS_MEMORY_LT_128BYTE_SELF	0x40000084
#define NATV_BUS_MEM_READ_ALL_ANY	0x40000085
#define NATV_BUS_MEM_READ_ALL_IO	0x40000086
#define NATV_BUS_MEM_READ_ALL_SELF	0x40000087
#define NATV_BUS_MEM_READ_BIL_ANY	0x40000088
#define NATV_BUS_MEM_READ_BIL_IO	0x40000089
#define NATV_BUS_MEM_READ_BIL_SELF	0x4000008a
#define NATV_BUS_MEM_READ_BRIL_ANY	0x4000008b
#define NATV_BUS_MEM_READ_BRIL_IO	0x4000008c
#define NATV_BUS_MEM_READ_BRIL_SELF	0x4000008d
#define NATV_BUS_MEM_READ_BRL_ANY	0x4000008e
#define NATV_BUS_MEM_READ_BRL_IO	0x4000008f
#define NATV_BUS_MEM_READ_BRL_SELF	0x40000090
#define NATV_BUS_MEM_READ_OUT_HI	0x40000091
#define NATV_BUS_MEM_READ_OUT_LO	0x40000092
#define NATV_BUS_OOQ_LIVE_REQ_HI	0x40000093
#define NATV_BUS_OOQ_LIVE_REQ_LO	0x40000094
#define NATV_BUS_RD_DATA_ANY	0x40000095
#define NATV_BUS_RD_DATA_IO	0x40000096
#define NATV_BUS_RD_DATA_SELF	0x40000097
#define NATV_BUS_RD_HIT	0x40000098
#define NATV_BUS_RD_HITM	0x40000099
#define NATV_BUS_RD_INVAL_ALL_HITM	0x4000009a
#define NATV_BUS_RD_INVAL_HITM	0x4000009b
#define NATV_BUS_RD_IO_ANY	0x4000009c
#define NATV_BUS_RD_IO_IO	0x4000009d
#define NATV_BUS_RD_IO_SELF	0x4000009e
#define NATV_BUS_RD_PRTL_ANY	0x4000009f
#define NATV_BUS_RD_PRTL_IO	0x400000a0
#define NATV_BUS_RD_PRTL_SELF	0x400000a1
#define NATV_BUS_SNOOPQ_REQ	0x400000a2
#define NATV_BUS_SNOOPS_ANY	0x400000a3
#define NATV_BUS_SNOOPS_IO	0x400000a4
#define NATV_BUS_SNOOPS_SELF	0x400000a5
#define NATV_BUS_SNOOPS_HITM_ANY	0x400000a6
#define NATV_BUS_SNOOPS_HITM_SELF	0x400000a7
#define NATV_BUS_SNOOP_STALL_CYCLES_ANY	0x400000a8
#define NATV_BUS_SNOOP_STALL_CYCLES_SELF	0x400000a9
#define NATV_BUS_WR_WB_ALL_ANY	0x400000aa
#define NATV_BUS_WR_WB_ALL_IO	0x400000ab
#define NATV_BUS_WR_WB_ALL_SELF	0x400000ac
#define NATV_BUS_WR_WB_CCASTOUT_ANY	0x400000ad
#define NATV_BUS_WR_WB_CCASTOUT_SELF	0x400000ae
#define NATV_BUS_WR_WB_EQ_128BYTE_ANY	0x400000af
#define NATV_BUS_WR_WB_EQ_128BYTE_IO	0x400000b0
#define NATV_BUS_WR_WB_EQ_128BYTE_SELF	0x400000b1
#define NATV_CPU_CPL_CHANGES	0x400000b2
#define NATV_CPU_CYCLES	0x400000b3
#define NATV_DATA_DEBUG_REGISTER_FAULT	0x400000b4
#define NATV_DATA_DEBUG_REGISTER_MATCHES	0x400000b5
#define NATV_DATA_EAR_ALAT	0x400000b6
#define NATV_DATA_EAR_CACHE_LAT1024	0x400000b7
#define NATV_DATA_EAR_CACHE_LAT128	0x400000b8
#define NATV_DATA_EAR_CACHE_LAT16	0x400000b9
#define NATV_DATA_EAR_CACHE_LAT2048	0x400000ba
#define NATV_DATA_EAR_CACHE_LAT256	0x400000bb
#define NATV_DATA_EAR_CACHE_LAT32	0x400000bc
#define NATV_DATA_EAR_CACHE_LAT4	0x400000bd
#define NATV_DATA_EAR_CACHE_LAT4096	0x400000be
#define NATV_DATA_EAR_CACHE_LAT512	0x400000bf
#define NATV_DATA_EAR_CACHE_LAT64	0x400000c0
#define NATV_DATA_EAR_CACHE_LAT8	0x400000c1
#define NATV_DATA_EAR_EVENTS	0x400000c2
#define NATV_DATA_EAR_TLB_ALL	0x400000c3
#define NATV_DATA_EAR_TLB_FAULT	0x400000c4
#define NATV_DATA_EAR_TLB_L2DTLB	0x400000c5
#define NATV_DATA_EAR_TLB_L2DTLB_OR_FAULT	0x400000c6
#define NATV_DATA_EAR_TLB_L2DTLB_OR_VHPT	0x400000c7
#define NATV_DATA_EAR_TLB_VHPT	0x400000c8
#define NATV_DATA_EAR_TLB_VHPT_OR_FAULT	0x400000c9
#define NATV_DATA_REFERENCES_SET0	0x400000ca
#define NATV_DATA_REFERENCES_SET1	0x400000cb
#define NATV_DISP_STALLED	0x400000cc
#define NATV_DTLB_INSERTS_HPW	0x400000cd
#define NATV_DTLB_INSERTS_HPW_RETIRED	0x400000ce
#define NATV_ENCBR_MISPRED_DETAIL_ALL_ALL_PRED	0x400000cf
#define NATV_ENCBR_MISPRED_DETAIL_ALL_CORRECT_PRED	0x400000d0
#define NATV_ENCBR_MISPRED_DETAIL_ALL_WRONG_PATH	0x400000d1
#define NATV_ENCBR_MISPRED_DETAIL_ALL_WRONG_TARGET	0x400000d2
#define NATV_ENCBR_MISPRED_DETAIL_ALL2_ALL_PRED	0x400000d3
#define NATV_ENCBR_MISPRED_DETAIL_ALL2_CORRECT_PRED	0x400000d4
#define NATV_ENCBR_MISPRED_DETAIL_ALL2_WRONG_PATH	0x400000d5
#define NATV_ENCBR_MISPRED_DETAIL_ALL2_WRONG_TARGET	0x400000d6
#define NATV_ENCBR_MISPRED_DETAIL_OVERSUB_ALL_PRED	0x400000d7
#define NATV_ENCBR_MISPRED_DETAIL_OVERSUB_CORRECT_PRED	0x400000d8
#define NATV_ENCBR_MISPRED_DETAIL_OVERSUB_WRONG_PATH	0x400000d9
#define NATV_ENCBR_MISPRED_DETAIL_OVERSUB_WRONG_TARGET	0x400000da
#define NATV_EXTERN_DP_PINS_0_TO_3_ALL	0x400000db
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN0	0x400000dc
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN0_OR_PIN1	0x400000dd
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN0_OR_PIN1_OR_PIN2	0x400000de
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN0_OR_PIN1_OR_PIN3	0x400000df
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN0_OR_PIN2	0x400000e0
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN0_OR_PIN2_OR_PIN3	0x400000e1
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN0_OR_PIN3	0x400000e2
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN1	0x400000e3
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN1_OR_PIN2	0x400000e4
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN1_OR_PIN2_OR_PIN3	0x400000e5
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN1_OR_PIN3	0x400000e6
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN2	0x400000e7
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN2_OR_PIN3	0x400000e8
#define NATV_EXTERN_DP_PINS_0_TO_3_PIN3	0x400000e9
#define NATV_EXTERN_DP_PINS_4_TO_5_ALL	0x400000ea
#define NATV_EXTERN_DP_PINS_4_TO_5_PIN4	0x400000eb
#define NATV_EXTERN_DP_PINS_4_TO_5_PIN5	0x400000ec
#define NATV_FE_BUBBLE_ALL	0x400000ed
#define NATV_FE_BUBBLE_ALLBUT_FEFLUSH_BUBBLE	0x400000ee
#define NATV_FE_BUBBLE_ALLBUT_IBFULL	0x400000ef
#define NATV_FE_BUBBLE_BRANCH	0x400000f0
#define NATV_FE_BUBBLE_BUBBLE	0x400000f1
#define NATV_FE_BUBBLE_FEFLUSH	0x400000f2
#define NATV_FE_BUBBLE_FILL_RECIRC	0x400000f3
#define NATV_FE_BUBBLE_GROUP1	0x400000f4
#define NATV_FE_BUBBLE_GROUP2	0x400000f5
#define NATV_FE_BUBBLE_GROUP3	0x400000f6
#define NATV_FE_BUBBLE_IBFULL	0x400000f7
#define NATV_FE_BUBBLE_IMISS	0x400000f8
#define NATV_FE_BUBBLE_TLBMISS	0x400000f9
#define NATV_FE_LOST_BW_ALL	0x400000fa
#define NATV_FE_LOST_BW_BI	0x400000fb
#define NATV_FE_LOST_BW_BRQ	0x400000fc
#define NATV_FE_LOST_BW_BR_ILOCK	0x400000fd
#define NATV_FE_LOST_BW_BUBBLE	0x400000fe
#define NATV_FE_LOST_BW_FEFLUSH	0x400000ff
#define NATV_FE_LOST_BW_FILL_RECIRC	0x40000100
#define NATV_FE_LOST_BW_IBFULL	0x40000101
#define NATV_FE_LOST_BW_IMISS	0x40000102
#define NATV_FE_LOST_BW_PLP	0x40000103
#define NATV_FE_LOST_BW_TLBMISS	0x40000104
#define NATV_FE_LOST_BW_UNREACHED	0x40000105
#define NATV_FP_FAILED_FCHKF	0x40000106
#define NATV_FP_FALSE_SIRSTALL	0x40000107
#define NATV_FP_FLUSH_TO_ZERO	0x40000108
#define NATV_FP_OPS_RETIRED	0x40000109
#define NATV_FP_TRUE_SIRSTALL	0x4000010a
#define NATV_HPW_DATA_REFERENCES	0x4000010b
#define NATV_IA32_INST_RETIRED	0x4000010c
#define NATV_IA32_ISA_TRANSITIONS	0x4000010d
#define NATV_IA64_INST_RETIRED	0x4000010e
#define NATV_IA64_INST_RETIRED_THIS	0x4000010f
#define NATV_IA64_TAGGED_INST_RETIRED_IBRP0_PMC8	0x40000110
#define NATV_IA64_TAGGED_INST_RETIRED_IBRP1_PMC9	0x40000111
#define NATV_IA64_TAGGED_INST_RETIRED_IBRP2_PMC8	0x40000112
#define NATV_IA64_TAGGED_INST_RETIRED_IBRP3_PMC9	0x40000113
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_ALL	0x40000114
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_BI	0x40000115
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_BRQ	0x40000116
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_BR_ILOCK	0x40000117
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_BUBBLE	0x40000118
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_FEFLUSH	0x40000119
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_FILL_RECIRC	0x4000011a
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_IBFULL	0x4000011b
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_IMISS	0x4000011c
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_PLP	0x4000011d
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_TLBMISS	0x4000011e
#define NATV_IDEAL_BE_LOST_BW_DUE_TO_FE_UNREACHED	0x4000011f
#define NATV_INST_CHKA_LDC_ALAT_ALL	0x40000120
#define NATV_INST_CHKA_LDC_ALAT_FP	0x40000121
#define NATV_INST_CHKA_LDC_ALAT_INT	0x40000122
#define NATV_INST_DISPERSED	0x40000123
#define NATV_INST_FAILED_CHKA_LDC_ALAT_ALL	0x40000124
#define NATV_INST_FAILED_CHKA_LDC_ALAT_FP	0x40000125
#define NATV_INST_FAILED_CHKA_LDC_ALAT_INT	0x40000126
#define NATV_INST_FAILED_CHKS_RETIRED_ALL	0x40000127
#define NATV_INST_FAILED_CHKS_RETIRED_FP	0x40000128
#define NATV_INST_FAILED_CHKS_RETIRED_INT	0x40000129
#define NATV_ISB_BUNPAIRS_IN	0x4000012a
#define NATV_ITLB_MISSES_FETCH_ALL	0x4000012b
#define NATV_ITLB_MISSES_FETCH_L1ITLB	0x4000012c
#define NATV_ITLB_MISSES_FETCH_L2ITLB	0x4000012d
#define NATV_L1DTLB_TRANSFER	0x4000012e
#define NATV_L1D_READS_SET0	0x4000012f
#define NATV_L1D_READS_SET1	0x40000130
#define NATV_L1D_READ_MISSES_ALL	0x40000131
#define NATV_L1D_READ_MISSES_RSE_FILL	0x40000132
#define NATV_L1ITLB_INSERTS_HPW	0x40000133
#define NATV_L1I_EAR_CACHE_LAT0	0x40000134
#define NATV_L1I_EAR_CACHE_LAT1024	0x40000135
#define NATV_L1I_EAR_CACHE_LAT128	0x40000136
#define NATV_L1I_EAR_CACHE_LAT16	0x40000137
#define NATV_L1I_EAR_CACHE_LAT256	0x40000138
#define NATV_L1I_EAR_CACHE_LAT32	0x40000139
#define NATV_L1I_EAR_CACHE_LAT4	0x4000013a
#define NATV_L1I_EAR_CACHE_LAT4096	0x4000013b
#define NATV_L1I_EAR_CACHE_LAT8	0x4000013c
#define NATV_L1I_EAR_CACHE_RAB	0x4000013d
#define NATV_L1I_EAR_EVENTS	0x4000013e
#define NATV_L1I_EAR_TLB_ALL	0x4000013f
#define NATV_L1I_EAR_TLB_FAULT	0x40000140
#define NATV_L1I_EAR_TLB_L2TLB	0x40000141
#define NATV_L1I_EAR_TLB_L2TLB_OR_FAULT	0x40000142
#define NATV_L1I_EAR_TLB_L2TLB_OR_VHPT	0x40000143
#define NATV_L1I_EAR_TLB_VHPT	0x40000144
#define NATV_L1I_EAR_TLB_VHPT_OR_FAULT	0x40000145
#define NATV_L1I_FETCH_ISB_HIT	0x40000146
#define NATV_L1I_FETCH_RAB_HIT	0x40000147
#define NATV_L1I_FILLS	0x40000148
#define NATV_L1I_PREFETCHES	0x40000149
#define NATV_L1I_PREFETCH_STALL_ALL	0x4000014a
#define NATV_L1I_PREFETCH_STALL_FLOW	0x4000014b
#define NATV_L1I_PURGE	0x4000014c
#define NATV_L1I_PVAB_OVERFLOW	0x4000014d
#define NATV_L1I_RAB_ALMOST_FULL	0x4000014e
#define NATV_L1I_RAB_FULL	0x4000014f
#define NATV_L1I_READS	0x40000150
#define NATV_L1I_SNOOP	0x40000151
#define NATV_L1I_STRM_PREFETCHES	0x40000152
#define NATV_L2DTLB_MISSES	0x40000153
#define NATV_L2_BAD_LINES_SELECTED_ANY	0x40000154
#define NATV_L2_BYPASS_L2_DATA1	0x40000155
#define NATV_L2_BYPASS_L2_DATA2	0x40000156
#define NATV_L2_BYPASS_L2_INST1	0x40000157
#define NATV_L2_BYPASS_L2_INST2	0x40000158
#define NATV_L2_BYPASS_L3_DATA1	0x40000159
#define NATV_L2_BYPASS_L3_INST1	0x4000015a
#define NATV_L2_DATA_REFERENCES_L2_ALL	0x4000015b
#define NATV_L2_DATA_REFERENCES_L2_DATA_READS	0x4000015c
#define NATV_L2_DATA_REFERENCES_L2_DATA_WRITES	0x4000015d
#define NATV_L2_FILLB_FULL_THIS	0x4000015e
#define NATV_L2_FORCE_RECIRC_ANY	0x4000015f
#define NATV_L2_FORCE_RECIRC_FILL_HIT	0x40000160
#define NATV_L2_FORCE_RECIRC_FRC_RECIRC	0x40000161
#define NATV_L2_FORCE_RECIRC_IPF_MISS	0x40000162
#define NATV_L2_FORCE_RECIRC_L1W	0x40000163
#define NATV_L2_FORCE_RECIRC_OZQ_MISS	0x40000164
#define NATV_L2_FORCE_RECIRC_SAME_INDEX	0x40000165
#define NATV_L2_FORCE_RECIRC_SMC_HIT	0x40000166
#define NATV_L2_FORCE_RECIRC_SNP_OR_L3	0x40000167
#define NATV_L2_FORCE_RECIRC_TAG_NOTOK	0x40000168
#define NATV_L2_FORCE_RECIRC_TRAN_PREF	0x40000169
#define NATV_L2_FORCE_RECIRC_VIC_BUF_FULL	0x4000016a
#define NATV_L2_FORCE_RECIRC_VIC_PEND	0x4000016b
#define NATV_L2_GOT_RECIRC_IFETCH_ANY	0x4000016c
#define NATV_L2_GOT_RECIRC_OZQ_ACC	0x4000016d
#define NATV_L2_IFET_CANCELS_ANY	0x4000016e
#define NATV_L2_IFET_CANCELS_BYPASS	0x4000016f
#define NATV_L2_IFET_CANCELS_CHG_PRIO	0x40000170
#define NATV_L2_IFET_CANCELS_DATA_RD	0x40000171
#define NATV_L2_IFET_CANCELS_DIDNT_RECIR	0x40000172
#define NATV_L2_IFET_CANCELS_IFETCH_BYP	0x40000173
#define NATV_L2_IFET_CANCELS_PREEMPT	0x40000174
#define NATV_L2_IFET_CANCELS_RECIR_OVER_SUB	0x40000175
#define NATV_L2_IFET_CANCELS_ST_FILL_WB	0x40000176
#define NATV_L2_INST_DEMAND_READS	0x40000177
#define NATV_L2_INST_PREFETCHES	0x40000178
#define NATV_L2_ISSUED_RECIRC_IFETCH_ANY	0x40000179
#define NATV_L2_ISSUED_RECIRC_OZQ_ACC	0x4000017a
#define NATV_L2_L3ACCESS_CANCEL_ANY	0x4000017b
#define NATV_L2_L3ACCESS_CANCEL_DFETCH	0x4000017c
#define NATV_L2_L3ACCESS_CANCEL_EBL_REJECT	0x4000017d
#define NATV_L2_L3ACCESS_CANCEL_FILLD_FULL	0x4000017e
#define NATV_L2_L3ACCESS_CANCEL_IFETCH	0x4000017f
#define NATV_L2_L3ACCESS_CANCEL_INV_L3_BYP	0x40000180
#define NATV_L2_L3ACCESS_CANCEL_SPEC_L3_BYP	0x40000181
#define NATV_L2_L3ACCESS_CANCEL_UC_BLOCKED	0x40000182
#define NATV_L2_MISSES	0x40000183
#define NATV_L2_OPS_ISSUED_FP_LOAD	0x40000184
#define NATV_L2_OPS_ISSUED_INT_LOAD	0x40000185
#define NATV_L2_OPS_ISSUED_NST_NLD	0x40000186
#define NATV_L2_OPS_ISSUED_RMW	0x40000187
#define NATV_L2_OPS_ISSUED_STORE	0x40000188
#define NATV_L2_OZDB_FULL_THIS	0x40000189
#define NATV_L2_OZQ_ACQUIRE	0x4000018a
#define NATV_L2_OZQ_CANCELS0_ANY	0x4000018b
#define NATV_L2_OZQ_CANCELS0_LATE_ACQUIRE	0x4000018c
#define NATV_L2_OZQ_CANCELS0_LATE_BYP_EFFRELEASE	0x4000018d
#define NATV_L2_OZQ_CANCELS0_LATE_RELEASE	0x4000018e
#define NATV_L2_OZQ_CANCELS0_LATE_SPEC_BYP	0x4000018f
#define NATV_L2_OZQ_CANCELS1_BANK_CONF	0x40000190
#define NATV_L2_OZQ_CANCELS1_CANC_L2M_ST	0x40000191
#define NATV_L2_OZQ_CANCELS1_CCV	0x40000192
#define NATV_L2_OZQ_CANCELS1_ECC	0x40000193
#define NATV_L2_OZQ_CANCELS1_HPW_IFETCH_CONF	0x40000194
#define NATV_L2_OZQ_CANCELS1_L1DF_L2M	0x40000195
#define NATV_L2_OZQ_CANCELS1_L1_FILL_CONF	0x40000196
#define NATV_L2_OZQ_CANCELS1_L2A_ST_MAT	0x40000197
#define NATV_L2_OZQ_CANCELS1_L2D_ST_MAT	0x40000198
#define NATV_L2_OZQ_CANCELS1_L2M_ST_MAT	0x40000199
#define NATV_L2_OZQ_CANCELS1_MFA	0x4000019a
#define NATV_L2_OZQ_CANCELS1_REL	0x4000019b
#define NATV_L2_OZQ_CANCELS1_SEM	0x4000019c
#define NATV_L2_OZQ_CANCELS1_ST_FILL_CONF	0x4000019d
#define NATV_L2_OZQ_CANCELS1_SYNC	0x4000019e
#define NATV_L2_OZQ_CANCELS2_ACQ	0x4000019f
#define NATV_L2_OZQ_CANCELS2_CANC_L2C_ST	0x400001a0
#define NATV_L2_OZQ_CANCELS2_CANC_L2D_ST	0x400001a1
#define NATV_L2_OZQ_CANCELS2_DIDNT_RECIRC	0x400001a2
#define NATV_L2_OZQ_CANCELS2_D_IFET	0x400001a3
#define NATV_L2_OZQ_CANCELS2_L2C_ST_MAT	0x400001a4
#define NATV_L2_OZQ_CANCELS2_L2FILL_ST_CONF	0x400001a5
#define NATV_L2_OZQ_CANCELS2_OVER_SUB	0x400001a6
#define NATV_L2_OZQ_CANCELS2_OZ_DATA_CONF	0x400001a7
#define NATV_L2_OZQ_CANCELS2_READ_WB_CONF	0x400001a8
#define NATV_L2_OZQ_CANCELS2_RECIRC_OVER_SUB	0x400001a9
#define NATV_L2_OZQ_CANCELS2_SCRUB	0x400001aa
#define NATV_L2_OZQ_CANCELS2_WEIRD	0x400001ab
#define NATV_L2_OZQ_FULL_THIS	0x400001ac
#define NATV_L2_OZQ_RELEASE	0x400001ad
#define NATV_L2_REFERENCES	0x400001ae
#define NATV_L2_STORE_HIT_SHARED_ANY	0x400001af
#define NATV_L2_SYNTH_PROBE	0x400001b0
#define NATV_L2_VICTIMB_FULL_THIS	0x400001b1
#define NATV_L3_LINES_REPLACED	0x400001b2
#define NATV_L3_MISSES	0x400001b3
#define NATV_L3_READS_ALL_ALL	0x400001b4
#define NATV_L3_READS_ALL_HIT	0x400001b5
#define NATV_L3_READS_ALL_MISS	0x400001b6
#define NATV_L3_READS_DATA_READ_ALL	0x400001b7
#define NATV_L3_READS_DATA_READ_HIT	0x400001b8
#define NATV_L3_READS_DATA_READ_MISS	0x400001b9
#define NATV_L3_READS_DINST_FETCH_ALL	0x400001ba
#define NATV_L3_READS_DINST_FETCH_HIT	0x400001bb
#define NATV_L3_READS_DINST_FETCH_MISS	0x400001bc
#define NATV_L3_READS_INST_FETCH_ALL	0x400001bd
#define NATV_L3_READS_INST_FETCH_HIT	0x400001be
#define NATV_L3_READS_INST_FETCH_MISS	0x400001bf
#define NATV_L3_REFERENCES	0x400001c0
#define NATV_L3_WRITES_ALL_ALL	0x400001c1
#define NATV_L3_WRITES_ALL_HIT	0x400001c2
#define NATV_L3_WRITES_ALL_MISS	0x400001c3
#define NATV_L3_WRITES_DATA_WRITE_ALL	0x400001c4
#define NATV_L3_WRITES_DATA_WRITE_HIT	0x400001c5
#define NATV_L3_WRITES_DATA_WRITE_MISS	0x400001c6
#define NATV_L3_WRITES_L2_WB_ALL	0x400001c7
#define NATV_L3_WRITES_L2_WB_HIT	0x400001c8
#define NATV_L3_WRITES_L2_WB_MISS	0x400001c9
#define NATV_LOADS_RETIRED	0x400001ca
#define NATV_MEM_READ_CURRENT_ANY	0x400001cb
#define NATV_MEM_READ_CURRENT_IO	0x400001cc
#define NATV_MISALIGNED_LOADS_RETIRED	0x400001cd
#define NATV_MISALIGNED_STORES_RETIRED	0x400001ce
#define NATV_NOPS_RETIRED	0x400001cf
#define NATV_PREDICATE_SQUASHED_RETIRED	0x400001d0
#define NATV_RSE_CURRENT_REGS_2_TO_0	0x400001d1
#define NATV_RSE_CURRENT_REGS_5_TO_3	0x400001d2
#define NATV_RSE_CURRENT_REGS_6	0x400001d3
#define NATV_RSE_DIRTY_REGS_2_TO_0	0x400001d4
#define NATV_RSE_DIRTY_REGS_5_TO_3	0x400001d5
#define NATV_RSE_DIRTY_REGS_6	0x400001d6
#define NATV_RSE_EVENT_RETIRED	0x400001d7
#define NATV_RSE_REFERENCES_RETIRED_ALL	0x400001d8
#define NATV_RSE_REFERENCES_RETIRED_LOAD	0x400001d9
#define NATV_RSE_REFERENCES_RETIRED_STORE	0x400001da
#define NATV_SERIALIZATION_EVENTS	0x400001db
#define NATV_STORES_RETIRED	0x400001dc
#define NATV_SYLL_NOT_DISPERSED_ALL	0x400001dd
#define NATV_SYLL_NOT_DISPERSED_EXPL	0x400001de
#define NATV_SYLL_NOT_DISPERSED_EXPL_OR_FE	0x400001df
#define NATV_SYLL_NOT_DISPERSED_EXPL_OR_FE_OR_MLI	0x400001e0
#define NATV_SYLL_NOT_DISPERSED_EXPL_OR_IMPL	0x400001e1
#define NATV_SYLL_NOT_DISPERSED_EXPL_OR_IMPL_OR_FE	0x400001e2
#define NATV_SYLL_NOT_DISPERSED_EXPL_OR_IMPL_OR_MLI	0x400001e3
#define NATV_SYLL_NOT_DISPERSED_EXPL_OR_MLI	0x400001e4
#define NATV_SYLL_NOT_DISPERSED_FE	0x400001e5
#define NATV_SYLL_NOT_DISPERSED_FE_OR_MLI	0x400001e6
#define NATV_SYLL_NOT_DISPERSED_IMPL	0x400001e7
#define NATV_SYLL_NOT_DISPERSED_IMPL_OR_FE	0x400001e8
#define NATV_SYLL_NOT_DISPERSED_IMPL_OR_FE_OR_MLI	0x400001e9
#define NATV_SYLL_NOT_DISPERSED_IMPL_OR_MLI	0x400001ea
#define NATV_SYLL_NOT_DISPERSED_MLI	0x400001eb
#define NATV_SYLL_OVERCOUNT_ALL	0x400001ec
#define NATV_SYLL_OVERCOUNT_EXPL	0x400001ed
#define NATV_SYLL_OVERCOUNT_IMPL	0x400001ee
#define NATV_UC_LOADS_RETIRED	0x400001ef
#define NATV_UC_STORES_RETIRED	0x400001f0
