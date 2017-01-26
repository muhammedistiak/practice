import pytest

def create_world():
    return []


def test_empty_world():
    world = create_world()
    assert world == []


def count_live_neighbours(all_neighbours, world):
    live_cell_count = 0
    for neighbour in all_neighbours:
        if neighbour in world:
            live_cell_count += 1
    return live_cell_count


def next_round(world):
    new_world = []
    for cell in world:
        all_neighbours = find_all_neighbours(cell)
        dead_cells = [cell for cell in all_neighbours if cell not in world]
        live_cell_count = count_live_neighbours(all_neighbours, world)
        if 2 <= live_cell_count <= 3:
            new_world.append(cell)
        for cell in dead_cells:
            if count_live_neighbours(cell) == 3:
                new_world.append(cell)
    return new_world


def find_all_neighbours(cell):
    nbs = []
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            nbs.append((cell[0] + dx, cell[1] + dy))

    nbs.remove(cell)
    return nbs


#################### tests #######
def test_count_zero_live_neighbours():
    world = [(1,1)]
    nbs = find_all_neighbours((1,1))
    assert 0 == count_live_neighbours(nbs, world)


def test_count_one_live_neighbours():
    world = [(0,0), (1,1)]
    nbs = find_all_neighbours((1,1))
    assert 1 == count_live_neighbours(nbs, world)


def test_non_empty_world():
    world = [(0,0), (1,1)]
    new_world = next_round(world)
    assert (0, 0) not in new_world


def test_find_all_neighbours():
    nb = find_all_neighbours((1,1))
    assert len(nb) == 8
    assert (0,0) in nb
    assert (-1,-1) not in nb
    
def test_live_with_two_nbs():
    world = [(0, 0), (0, 1), (1, 1)]
    new_world = next_round(world)
    assert len(new_world) == 3
    assert (0, 0) in new_world

def test_dying_cell_for_four_nbs():
    world = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1)]
    new_world = next_round(world)
    assert len(new_world) == 3
    assert (1, 1) not in new_world