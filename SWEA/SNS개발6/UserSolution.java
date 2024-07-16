package SNS개발6;

import java.util.*;

class UserSolution {
    static final int MAXL = 5;
    static final int MAXF = 10;
    
    private Map<Integer, Set<Integer>> friends;

    public void init(int N) {
        friends = new HashMap<>();
        for (int i = 1; i <= N; i++) {
            friends.put(i, new HashSet<>());
        }
    }

    public void add(int id, int F, int ids[]) {
        Set<Integer> friendList = friends.get(id);
        for (int i = 0; i < F; i++) {
            int friendId = ids[i];
            friendList.add(friendId);
            friends.get(friendId).add(id);
        }
    }

    public void del(int id1, int id2) {
        friends.get(id1).remove(id2);
        friends.get(id2).remove(id1);
    }

    public int recommend(int id, int list[]) {
        Set<Integer> userFriends = friends.get(id);
        Map<Integer, Integer> mutualFriendsCount = new HashMap<>();

        for (int friend : userFriends) {
            for (int mutualFriend : friends.get(friend)) {
                if (mutualFriend != id && !userFriends.contains(mutualFriend)) {
                    mutualFriendsCount.put(mutualFriend, mutualFriendsCount.getOrDefault(mutualFriend, 0) + 1);
                }
            }
        }

        List<Map.Entry<Integer, Integer>> sortedMutualFriends = new ArrayList<>(mutualFriendsCount.entrySet());
        sortedMutualFriends.sort((a, b) -> {
            if (a.getValue().equals(b.getValue())) {
                return Integer.compare(a.getKey(), b.getKey());
            } else {
                return Integer.compare(b.getValue(), a.getValue());
            }
        });

        int recommendationCount = 0;
        for (int i = 0; i < Math.min(MAXL, sortedMutualFriends.size()); i++) {
            list[i] = sortedMutualFriends.get(i).getKey();
            recommendationCount++;
        }

        return recommendationCount;
    }
}
