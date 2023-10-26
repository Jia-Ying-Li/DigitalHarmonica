################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../source/TSISensor.c \
../source/lcd.c \
../source/main.c \
../source/mtb.c \
../source/semihost_hardfault.c \
../source/slcd.c \
../source/utils.c 

C_DEPS += \
./source/TSISensor.d \
./source/lcd.d \
./source/main.d \
./source/mtb.d \
./source/semihost_hardfault.d \
./source/slcd.d \
./source/utils.d 

OBJS += \
./source/TSISensor.o \
./source/lcd.o \
./source/main.o \
./source/mtb.o \
./source/semihost_hardfault.o \
./source/slcd.o \
./source/utils.o 


# Each subdirectory must supply rules for building sources it contributes
source/%.o: ../source/%.c source/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -DCPU_MKL46Z256VLL4_cm0plus -DCPU_MKL46Z256VLL4 -DFSL_RTOS_BM -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=1 -DCR_INTEGER_PRINTF -DPRINTF_FLOAT_ENABLE=0 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -D__REDLIB__ -I"/Users/jiayingli/Downloads/SP2023/CS3420/FinalProject/board" -I"/Users/jiayingli/Downloads/SP2023/CS3420/FinalProject/source" -I"/Users/jiayingli/Downloads/SP2023/CS3420/FinalProject" -I"/Users/jiayingli/Downloads/SP2023/CS3420/FinalProject/drivers" -I"/Users/jiayingli/Downloads/SP2023/CS3420/FinalProject/CMSIS" -I"/Users/jiayingli/Downloads/SP2023/CS3420/FinalProject/utilities" -I"/Users/jiayingli/Downloads/SP2023/CS3420/FinalProject/startup" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m0plus -mthumb -D__REDLIB__ -fstack-usage -specs=redlib.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-source

clean-source:
	-$(RM) ./source/TSISensor.d ./source/TSISensor.o ./source/lcd.d ./source/lcd.o ./source/main.d ./source/main.o ./source/mtb.d ./source/mtb.o ./source/semihost_hardfault.d ./source/semihost_hardfault.o ./source/slcd.d ./source/slcd.o ./source/utils.d ./source/utils.o

.PHONY: clean-source

