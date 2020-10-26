//
//  Generated file. Do not edit.
//

#import "GeneratedPluginRegistrant.h"

#if __has_include(<flutter_android_pip/FlutterAndroidPipPlugin.h>)
#import <flutter_android_pip/FlutterAndroidPipPlugin.h>
#else
@import flutter_android_pip;
#endif

#if __has_include(<screen/ScreenPlugin.h>)
#import <screen/ScreenPlugin.h>
#else
@import screen;
#endif

#if __has_include(<youtube_player/YoutubePlayerPlugin.h>)
#import <youtube_player/YoutubePlayerPlugin.h>
#else
@import youtube_player;
#endif

@implementation GeneratedPluginRegistrant

+ (void)registerWithRegistry:(NSObject<FlutterPluginRegistry>*)registry {
  [FlutterAndroidPipPlugin registerWithRegistrar:[registry registrarForPlugin:@"FlutterAndroidPipPlugin"]];
  [ScreenPlugin registerWithRegistrar:[registry registrarForPlugin:@"ScreenPlugin"]];
  [YoutubePlayerPlugin registerWithRegistrar:[registry registrarForPlugin:@"YoutubePlayerPlugin"]];
}

@end
