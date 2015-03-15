#pragma once

#include <vector>
#include <stack>
#include <queue>

namespace Graph {
	struct Vertex {
		int 					m_Value;
		std::vector<Vertex*> 	m_LinkedVertex;
		bool 					m_CheckedFlag;
	};

	// preorder
	static void DFS( Vertex* source ) {
		if ( source == nullptr )
			return;

		std::stack<Vertex*> prevVertex;
		Vertex* currentVertex = source;
		bool rewindStack = false;

		do {
			if ( !currentVertex->m_CheckedFlag ) {
				printf( "%d ", currentVertex->m_Value );
				currentVertex->m_CheckedFlag = true;
			}

			rewindStack = true;
			for each ( auto each in currentVertex->m_LinkedVertex ) {
				if ( !each->m_CheckedFlag ) {
					prevVertex.push( currentVertex );
					currentVertex = each;

					rewindStack = false;
					break;
				}
			}

			if ( rewindStack ) {
				currentVertex = prevVertex.top( );
				prevVertex.pop( );
			}
		} while ( !prevVertex.empty( ) );
	} 

	static void BFS( Vertex* source ) {
		if ( source == nullptr )
			return;

		std::queue<Vertex*> queue;

		queue.push( source );
		Vertex* currentVertex = nullptr;

		while ( !queue.empty( ) ) {
			currentVertex = queue.front( );
			queue.pop( );

			printf( "%d ", currentVertex->m_Value );

			for each ( auto each in currentVertex->m_LinkedVertex ) {
				if ( !each->m_CheckedFlag ) {
					each->m_CheckedFlag = true;
					queue.push( each );
				}
			}

		}
	}

	static void test( ) {
		const int VERTEX_NUMBER = 6;

		Graph::Vertex vertexList[VERTEX_NUMBER];
		for ( int i = 0; i < VERTEX_NUMBER; ++i ) {
			vertexList[i].m_Value = i;
		}

		vertexList[0].m_LinkedVertex.push_back( &vertexList[1] );
		vertexList[0].m_LinkedVertex.push_back( &vertexList[3] );

		vertexList[1].m_LinkedVertex.push_back( &vertexList[4] );

		vertexList[2].m_LinkedVertex.push_back( &vertexList[5] );

		vertexList[3].m_LinkedVertex.push_back( &vertexList[1] );

		vertexList[4].m_LinkedVertex.push_back( &vertexList[2] );
		vertexList[4].m_LinkedVertex.push_back( &vertexList[3] );

		vertexList[5].m_LinkedVertex.push_back( &vertexList[5] );

		for ( int i = 0; i < VERTEX_NUMBER; ++i ) {
			vertexList[i].m_CheckedFlag = false;
		}

		printf( "DFS :\n" );
		Graph::DFS( &vertexList[0] );

		for ( int i = 0; i < VERTEX_NUMBER; ++i ) {
			vertexList[i].m_CheckedFlag = false;
		}

		printf( "\n\n" );

		printf( "BFS :\n" );
		Graph::BFS( &vertexList[0] );
	}
}
