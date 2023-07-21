<?php

function getData(string $data): array
{
	$letters = [];

	for ($x = 0; $x < strlen($data); $x++) {
		$letters[] = $data[$x];
	}
	return $letters;
}

function letterCount(string $data): int
{
	return count(getData($data));
}

function getPacketMarker(string $data): void
{
	$SOP = [];

	for ($x = 0; $x < letterCount($data); $x++) {
		while ($x < 4) {
			$SOP[] = getData($data[$x]);
			break;
		}
		if ($x >= 4) {
			if ($SOP[0] === $SOP[1] ||
				$SOP[0] === $SOP[2] ||
				$SOP[0] === $SOP[3] ||
				$SOP[1] === $SOP[2] ||
				$SOP[1] === $SOP[3] ||
				$SOP[2] === $SOP[3])
			{
				array_shift($SOP);
				$SOP[] = getData($data[$x]);
			} else {
				echo 'First start-of-package marker occurs at position ' . $x . ".\n";
				break;
			}
		}
	}
}

function getMessageMarker(string $data): void
{
	$SOM = [];
	$arr = [];

	for ($x = 0; $x < letterCount($data); $x++) {
		while ($x < 14) {
			$SOM[] = getData($data[$x]);
			break;
		}
		if ($x >= 14) {
			if ($SOM[0] === $SOM[1] ||
				$SOM[0] === $SOM[2] ||
				$SOM[0] === $SOM[3] ||
				$SOM[0] === $SOM[4] ||
				$SOM[0] === $SOM[5] ||
				$SOM[0] === $SOM[6] ||
				$SOM[0] === $SOM[7] ||
				$SOM[0] === $SOM[8] ||
				$SOM[0] === $SOM[9] ||
				$SOM[0] === $SOM[10] ||
				$SOM[0] === $SOM[11] ||
				$SOM[0] === $SOM[12] ||
				$SOM[0] === $SOM[13] ||
				$SOM[1] === $SOM[2] ||
				$SOM[1] === $SOM[3] ||
				$SOM[1] === $SOM[4] ||
				$SOM[1] === $SOM[5] ||
				$SOM[1] === $SOM[6] ||
				$SOM[1] === $SOM[7] ||
				$SOM[1] === $SOM[8] ||
				$SOM[1] === $SOM[9] ||
				$SOM[1] === $SOM[10] ||
				$SOM[1] === $SOM[11] ||
				$SOM[1] === $SOM[12] ||
				$SOM[1] === $SOM[13] ||
				$SOM[2] === $SOM[3] ||
				$SOM[2] === $SOM[4] ||
				$SOM[2] === $SOM[5] ||
				$SOM[2] === $SOM[6] ||
				$SOM[2] === $SOM[7] ||
				$SOM[2] === $SOM[8] ||
				$SOM[2] === $SOM[9] ||
				$SOM[2] === $SOM[10] ||
				$SOM[2] === $SOM[11] ||
				$SOM[2] === $SOM[12] ||
				$SOM[2] === $SOM[13] ||
				$SOM[3] === $SOM[4] ||
				$SOM[3] === $SOM[5] ||
				$SOM[3] === $SOM[6] ||
				$SOM[3] === $SOM[7] ||
				$SOM[3] === $SOM[8] ||
				$SOM[3] === $SOM[9] ||
				$SOM[3] === $SOM[10] ||
				$SOM[3] === $SOM[11] ||
				$SOM[3] === $SOM[12] ||
				$SOM[3] === $SOM[13] ||
				$SOM[4] === $SOM[5] ||
				$SOM[4] === $SOM[6] ||
				$SOM[4] === $SOM[7] ||
				$SOM[4] === $SOM[8] ||
				$SOM[4] === $SOM[9] ||
				$SOM[4] === $SOM[10] ||
				$SOM[4] === $SOM[11] ||
				$SOM[4] === $SOM[12] ||
				$SOM[4] === $SOM[13] ||
				$SOM[5] === $SOM[6] ||
				$SOM[5] === $SOM[7] ||
				$SOM[5] === $SOM[8] ||
				$SOM[5] === $SOM[9] ||
				$SOM[5] === $SOM[10] ||
				$SOM[5] === $SOM[11] ||
				$SOM[5] === $SOM[12] ||
				$SOM[5] === $SOM[13] ||
				$SOM[6] === $SOM[7] ||
				$SOM[6] === $SOM[8] ||
				$SOM[6] === $SOM[9] ||
				$SOM[6] === $SOM[10] ||
				$SOM[6] === $SOM[11] ||
				$SOM[6] === $SOM[12] ||
				$SOM[6] === $SOM[13] ||
				$SOM[7] === $SOM[8] ||
				$SOM[7] === $SOM[9] ||
				$SOM[7] === $SOM[10] ||
				$SOM[7] === $SOM[11] ||
				$SOM[7] === $SOM[12] ||
				$SOM[7] === $SOM[13] ||
				$SOM[8] === $SOM[9] ||
				$SOM[8] === $SOM[10] ||
				$SOM[8] === $SOM[11] ||
				$SOM[8] === $SOM[12] ||
				$SOM[8] === $SOM[13] ||
				$SOM[9] === $SOM[10] ||
				$SOM[9] === $SOM[11] ||
				$SOM[9] === $SOM[12] ||
				$SOM[9] === $SOM[13] ||
				$SOM[10] === $SOM[11] ||
				$SOM[10] === $SOM[12] ||
				$SOM[10] === $SOM[13] ||
				$SOM[11] === $SOM[12] ||
				$SOM[11] === $SOM[13] ||
				$SOM[12] === $SOM[13])
			{
				array_shift($SOM);
				$SOM[] = getData($data[$x]);
			} else {
				echo 'First start-of-message marker occurs at position ' . $x . ".\n";
				break;
			}
		}
	}
}

$file = 'input.txt';
$handle = fopen($file, 'r');
$data = fread($handle, filesize($file));

getData($data);
letterCount($data);
getPacketMarker($data);
getMessageMarker($data);

fclose($handle);
