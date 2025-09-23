def solution(bandage, health, attacks):
    cast_time, heal_per_sec, bonus_heal = bandage
    
    max_health = health
    current_health = health
    last_event_time = 0

    for attack_time, damage in attacks:
        time_diff = attack_time - last_event_time - 1

        if time_diff > 0:
            current_health += time_diff * heal_per_sec
            bonus_count = time_diff // cast_time
            current_health += bonus_count * bonus_heal
            
            if current_health > max_health:
                current_health = max_health

        current_health -= damage
        
        if current_health <= 0:
            return -1
        
        last_event_time = attack_time
        
    return current_health