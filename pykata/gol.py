import pytest

def create_world():
    return []


def test_empty_world():
    world = create_world()
    assert world == []


def count_live_neighbours(all_neighbours):
	live_cell_count = 0
	for neighbour in all_neighbours:
 		if neighbour in world:
 			live_cell_count += 1
 	return live_cell_count


def next_round(world):
 	for cell in world:
 		all_neighbours = find_all_neighbours(cell)
 		live_cell_count = count_live_neighbours(all_neighbours)

 	return []


def find_all_neighbours(cell):
	nbs = []
	for dx in [-1,0,1]:
		for dy in [-1,0,1]:
			nbs.append((cell[0] + dx, cell[1] + dy))

	nbs.remove(cell)
	return nbs


#################### tests #######
def test_count_live_neighbours():
	assert False


def test_non_empty_world():
    world = [(0,0), (1,1)]
    new_world = next_round(world)
    assert (0, 0) not in new_world


def test_find_all_neighbours():
	nb = find_all_neighbours((1,1))
	assert len(nb) == 8
	assert (0,0) in nb
	assert (-1,-1) not in nb
	