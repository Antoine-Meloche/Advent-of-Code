#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

bool is_digit(char c) {
	if ( c >= '0' && c <= '9' ) {
		return true;
	}
	return false;
}

int part_one(FILE* fp) {
	int ans = 0;

	char *line = NULL;
	size_t len = 0;
	ssize_t read;

	while ( (read = getline(&line, &len, fp)) != -1 ) {
		int i;
		int first_num = 99;
		int last_num = 0;

		for ( i=0; i < len; i++ ) {
			if ( is_digit(line[i]) ) {
				if ( first_num == 99 ) {
					first_num = line[i] - '0';
				}
				last_num = line[i] - '0';
			}
		}

		ans += (first_num * 10) + last_num;
		line = NULL;
	}

	free(line);
	return ans;
}

bool prefix(const char *pref, const char *str) {
	return strncmp(pref, str, strlen(pref)) == 0;
}

int string_to_num(char *str) {
	if ( prefix("one", str) ) {
		return 1;
	}
	if ( prefix("two", str) ) {
		return 2;
	}
	if ( prefix("three", str) ) {
		return 3;
	}
	if ( prefix("four", str) ) {
		return 4;
	}
	if ( prefix("five", str) ) {
		return 5;
	}
	if ( prefix("six", str) ) {
		return 6;
	}
	if ( prefix("seven", str) ) {
		return 7;
	}
	if ( prefix("eight", str) ) {
		return 8;
	}
	if ( prefix("nine", str) ) {
		return 9;
	}
	if ( prefix("zero", str) ) {
		return 0;
	}
	return -1;
}

int part_two(FILE* fp) {
	int ans = 0;

	char *line = NULL;
	size_t len = 0;
	ssize_t read;

	while ( (read = getline(&line, &len, fp)) != -1 ) {
		int i;
		int first_num = 99;
		int last_num = 0;

		for ( i=0; i < len; i++ ) {
			if ( is_digit(line[i]) ) {
				if ( first_num == 99 ) {
					first_num = line[i] - '0';
				}
				last_num = line[i] - '0';
			} else {
				int snum = string_to_num(line + i);

				if ( snum != -1 ) {
					if ( first_num == 99 ) {
						first_num = snum;
					}
					last_num = snum;
				}
			}
		}

		ans += (first_num * 10) + last_num;
		line = NULL;
	}

	return ans;
}

void main() {
	FILE *fp;
	fp = fopen("input.txt", "r");
	if ( fp == NULL ) {
		printf("Could not open file 'input.txt'");
		exit(1);
	}

	int ans_one = part_one(fp);
	printf("Part 1: %d\n", ans_one);

	fp = fopen("input.txt", "r");
	if ( fp == NULL ) {
		printf("Could not open file 'input.txt'");
		exit(1);
	}

	int ans_two = part_two(fp);
	printf("Part 2: %d\n", ans_two);

	fclose(fp);
}
