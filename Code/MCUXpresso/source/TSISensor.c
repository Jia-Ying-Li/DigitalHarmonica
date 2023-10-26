#include <MKL46Z4.h>
#include <TSISensor.h>
#include "LCD.h"

// Many thanks to the helpful TSI documentation from various examples at RIT and NXP community 

void TSI_Init(void){

	SIM->SCGC5 |= SIM_SCGC5_TSI_MASK;   //enable clock

	TSI0->GENCS = TSI_GENCS_OUTRGF_MASK // clear out of range flag

							|	TSI_GENCS_MODE(0)			
							|	TSI_GENCS_REFCHRG(0)
							|	TSI_GENCS_DVOLT(0)	
							|	TSI_GENCS_EXTCHRG(0)  
							|	TSI_GENCS_PS(0)		
							|	TSI_GENCS_NSCN(31)	

							|	TSI_GENCS_TSIEN_MASK	
							//| TSI_GENCS_STPE_MASK  
							| TSI_GENCS_EOSF_MASK;
}

int TSI_Scan(void){
	int data;
	TSI0->DATA = TSI_DATA_TSICH(10)		
						 | TSI_DATA_SWTS_MASK;
	data = (TSI0->DATA & 0xFFFF) - 625;
														
		TSI0->GENCS |= TSI_GENCS_EOSF_MASK ; 
	return data;
}
