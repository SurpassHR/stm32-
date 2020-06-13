#ifndef  __BIT_BAND_H__
#define  __BIT_BAND_H__

 
#define output_addr_offset 0x14
#define input_addr_offset 0x10

#define PAout(n)  ( *((	unsigned int *)(0x42000000 +((GPIOA_BASE + output_addr_offset)-0x40000000) *8*4 +n*4)))
#define PBout(n)  ( *((	unsigned int *)(0x42000000 +((GPIOB_BASE + output_addr_offset)-0x40000000) *8*4 +n*4)))
#define PCout(n)  ( *((	unsigned int *)(0x42000000 +((GPIOC_BASE + output_addr_offset)-0x40000000) *8*4 +n*4)))
#define PDout(n)  ( *((	unsigned int *)(0x42000000 +((GPIOD_BASE + output_addr_offset)-0x40000000) *8*4 +n*4)))
#define PEout(n)  ( *((	unsigned int *)(0x42000000 +((GPIOE_BASE + output_addr_offset)-0x40000000) *8*4 +n*4)))
#define PFout(n)  ( *((	unsigned int *)(0x42000000 +((GPIOF_BASE + output_addr_offset)-0x40000000) *8*4 +n*4)))
#define PGout(n)  ( *((	unsigned int *)(0x42000000 +((GPIOG_BASE + output_addr_offset)-0x40000000) *8*4 +n*4)))
#define PHout(n)  ( *((	unsigned int *)(0x42000000 +((GPIOH_BASE + output_addr_offset)-0x40000000) *8*4 +n*4)))
#define PIout(n)  ( *((	unsigned int *)(0x42000000 +((GPIOI_BASE + output_addr_offset)-0x40000000) *8*4 +n*4)))


#define  PAin(n)  ( *((	unsigned int *)(0x42000000 +((GPIOA_BASE + input_addr_offset )-0x40000000) *8*4 +n*4)))
#define  PBin(n)  ( *((	unsigned int *)(0x42000000 +((GPIOB_BASE + input_addr_offset )-0x40000000) *8*4 +n*4)))
#define  PCin(n)  ( *((	unsigned int *)(0x42000000 +((GPIOC_BASE + input_addr_offset )-0x40000000) *8*4 +n*4)))
#define  PDin(n)  ( *((	unsigned int *)(0x42000000 +((GPIOD_BASE + input_addr_offset )-0x40000000) *8*4 +n*4)))
#define  PEin(n)  ( *((	unsigned int *)(0x42000000 +((GPIOE_BASE + input_addr_offset )-0x40000000) *8*4 +n*4)))
#define  PFin(n)  ( *((	unsigned int *)(0x42000000 +((GPIOF_BASE + input_addr_offset )-0x40000000) *8*4 +n*4)))
#define  PGin(n)  ( *((	unsigned int *)(0x42000000 +((GPIOG_BASE + input_addr_offset )-0x40000000) *8*4 +n*4)))
#define  PHin(n)  ( *((	unsigned int *)(0x42000000 +((GPIOH_BASE + input_addr_offset )-0x40000000) *8*4 +n*4)))
#define  PIin(n)  ( *((	unsigned int *)(0x42000000 +((GPIOI_BASE + input_addr_offset )-0x40000000) *8*4 +n*4)))

	




#endif
