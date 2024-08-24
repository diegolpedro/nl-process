###############################################################################
TRACK0=@fibertel
TRACK1=@Apple
TRACK2=@vwargentina
TRACK3=@Aerolineas_AR
CANT=50
FILE0=$(CANT)tws_$(TRACK0).csv
FILE1=$(CANT)tws_$(TRACK1).csv
FILE2=$(CANT)tws_$(TRACK2).csv
FILE3=$(CANT)tws_$(TRACK3).csv
DOWN_BIN=twreader.py
PROCESS_BIN=nlprocess.py
###############################################################################
OPERATIONS= clean generate process

###############################################################################
.PHONY: all
all: $(OPERATIONS)

.PHONY: process
process: $(FILE0) $(FILE1) $(FILE2) $(FILE3)
	./$(PROCESS_BIN) $(FILE0)
	./$(PROCESS_BIN) $(FILE1)
	./$(PROCESS_BIN) $(FILE2)
	./$(PROCESS_BIN) $(FILE3)

.PHONY: generate
generate: $(FILE0) $(FILE1) $(FILE2) $(FILE3)

$(FILE0):
	./$(DOWN_BIN) $(TRACK0) $(CANT)
$(FILE1):
	./$(DOWN_BIN) $(TRACK1) $(CANT)
$(FILE2):
	./$(DOWN_BIN) $(TRACK2) $(CANT)
$(FILE3):
	./$(DOWN_BIN) $(TRACK3) $(CANT)

.PHONY: clean
clean:
	rm *.csv
