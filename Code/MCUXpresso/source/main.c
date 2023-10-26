#include <pin_mux.h>
#include <clock_config.h>
#include <stdio.h>
#include <board.h>
#include <MKL46Z4.h>
#include <fsl_debug_console.h>
#include <stdio.h>
#include <TSISensor.h>
#include <MKL46Z4.h>
#include "utils.h"

/*------------------------------*/
/* UART communication functions */
/*------------------------------*/
/* Initialize the UART for TX (115200, 8N1) */

void init_uart(void)
{
	//Use UART port through debug interface
	// Connect to UART with TX (115200, 8N1)

	BOARD_InitBootPins();
    BOARD_InitBootClocks();
 	BOARD_InitDebugConsole();
}

void uart_putc (char ch)
{
	/* Wait until space is available in the FIFO */
	while(!(UART0->S1 & UART_S1_TDRE_MASK));
	/* Send the character */
	UART0->D = (uint8_t)ch;
}

void uart_puts(char *ptr_str)
{
    while(*ptr_str){
			/* Replace newlines with \r\n carriage return */
			if(*ptr_str == '\n') { uart_putc('\r'); }
      uart_putc(*ptr_str++);
		}
}

void short_delay()
{
	for(int i=1000000; i>0; i--){}
}

/*------------------------------*/

int main(void) {
	TSI_Init();

	init_uart();
	char cnt=0;

/* Transmit FRDM-KL46Z Input to Python Implementation */
	while(1){
		short_delay();
		cnt++;
		uart_putc(cnt);

		int x;
		x = TSI_Scan();

		if (x > 100 && x < 162.5) {
			uart_putc('c');
		}
		else if (x > 162.5 &&x < 325 ) {
			uart_putc('D');
		}
		else if (x > 325 && x < 487.5) {
			uart_putc('E');
		}
		else if (x > 487.5 && x < 650) {
			uart_putc('F');
		}
		else if (x > 650 && x < 812.5) {
			uart_putc('G');
		}
		else if (x > 812.5 && x < 975){
			uart_putc('A');
		}
		else if (x > 975 && x < 1137.5) {
			uart_putc('B');
		}
		else if (x > 1137.5 && x < 1300) {
			uart_putc('C');
		}
	}
	return 0 ;
}
