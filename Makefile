bin = $(shell npm bin)
dollphie = "$(bin)/dollphie"


# -- Configuration -----------------------------------------------------
SRC_DIR = game
DOC_DIR = docs/source
SRC     = $(wildcard $(SRC_DIR)/*.rpy $(SRC_DIR)/**/*.rpy)
TGT     = ${SRC:$(SRC_DIR)/%.rpy=$(DOC_DIR)/%.rst}


# -- Compilation -------------------------------------------------------
$(DOC_DIR)/%.rst: $(SRC_DIR)/%.rpy
	mkdir -p $(dir $@)
	$(dollphie) --input python --output sphinx "$<" > "$@"

node_modules: package.json
	npm install


# -- Tasks -------------------------------------------------------------
documentation: node_modules $(TGT)
	cd docs && "$(MAKE)" html

clean:
	rm -f $(TGT) game/*.rpyc game/**/*.rpyc game/*.rpyb game/*.bak

.PHONY: clean documentation
