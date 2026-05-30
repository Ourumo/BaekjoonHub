def solution(skill, skill_trees):
    result = 0
    for skill_tree in skill_trees:
        tmp_skill = []
        for s in skill_tree:
            if s in skill:
                tmp_skill.append(s)

        new_skill_trees = "".join(tmp_skill)

        if skill.startswith(new_skill_trees):
            result += 1

    return result