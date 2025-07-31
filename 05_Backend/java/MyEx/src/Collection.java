import java.util.*;

public class Collection {

	public static void main(String[] args) {
		// List 컬렉션 : 요소를 인덱스로 관리. ArrayList, Vector, LinkedList 등.
		// add, set, contains, get, isEmpty, size, clear, remove
		// ArrayList : 배열과 비슷. 동적 크기.
		// Vector : ArrayList와 내부 구조는 동일하나 동기화된 메서드로 구성되어 있어 여러 스레드가 동시에 vector 메서드를 실행 할 수 없음.
		// LinkedList : ArrayList와 동일하지만, 내부 구조는 다름. 인접 요소를 연결해서 관리함. 빈번한 요소 삭제, 삽입이 있을 때 효율이 좋음.
		
		// ---------------------------------------------------------
		
		// Set 컬렉션 : 저장 순서 유지x. 요소 중복 저장x. HashSet, LinkedHashSet, TreeSet 등. 
		// add, contains, isEmpty, iterator, size, clear, remove
		// HashSet : hashCode()와 equals()의 반환 값 모두 true이면 동일한 객체로 판단하여 중복 저장하지 않음. 두 메서드는 재정의하여 원하는대로 사용 가능.
		// iterator : Set 컬렉션 객체를 가져오는 반복자 객체. 
		Set<Integer> set = new HashSet<>();
		set.add(1);
		set.add(2);
		set.add(3);
		Iterator<Integer> it = set.iterator();
		
		while (it.hasNext()) {
			Integer n = it.next();
			System.out.println(n);
			it.remove();
		}
		
		// ---------------------------------------------------------
		
		// Map 컬렉션 : 키와 값으로 구성된 엔트리 객체를 저장. HashMap, Hashtable, LinkedHashMap, Properties, TreeMap 등.
		// put, containsKey, containsValue, entrySet, get, isEmpty, keySet, size, values, clear, remove
		// HashMap
		// Hashtable
		// properties : Hashtable의 자식 클래스. 

		// ---------------------------------------------------------
		
		// 검색 기능을 강화한 컬렉션 : TreeSet, TreeMap
		// TreeSet : 이진 트리 기반 Set 컬렉션. 부모보다 낮은 자식은 left, 높은 자식은 right 노드에 저장.
		// first, last, lower, higher, floor, ceiling, pollFirst, pollLast, descendingIterator, descendingSet, headSet, tailSet, subSet.
		TreeSet<Integer> scores = new TreeSet<>();
		scores.add(89);
		scores.add(94);
		scores.add(83);
		scores.add(48);
		scores.add(59);
		
		// 요소 가져오기
		for (Integer s : scores) {
			System.out.println(s + " ");
		}
		System.out.println("가장 낮은 점수: " + scores.first());
		System.out.println("가장 높은 점수: " + scores.last());
		System.out.println("80점 아래 점수: " + scores.lower(80));
		System.out.println("80점 위의 점수: " + scores.higher(80));
		System.out.println("80점이거나 바로 아래 점수: " + scores.floor(80));
		System.out.println("80점이거나 바로 위 점수: " + scores.ceiling(80));
		
		// TreeMap : TreeSet과의 차이점은 키와 값으로 된 엔트리를 저장하고, 키 값을 기준으로 정렬한다.
		
		// ---------------------------------------------------------
		
		// LIFO, FIFO 컬렉션
		// Stack : LIFO. 
		// push, pop
		Stack<Integer> stck = new Stack<>();
		stck.push(1);
		stck.push(2);
		stck.push(3);
		
		while (!stck.isEmpty()) {
			System.out.println(stck.pop());
		}
		
		// Queue : FIFO. Queue 인터페이스를 구현한 대표적인 클래스가 LinkedList.
		// offer, poll
		Queue<Integer> que = new LinkedList<>();
		que.offer(1);
		que.offer(2);
		que.offer(3);
		
		while (!que.isEmpty()) {
			System.out.println(que.poll());
		}
		
		
		
		
		
		
		
				
		

	}

}
